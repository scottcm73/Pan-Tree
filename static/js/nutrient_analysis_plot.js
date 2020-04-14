// Plotly.d3.json('/nutrient_per_order', function(rows){
//     function assignOptions(dateArray, selector) {
//             for (var i = 0; i < dateArray.length;  i++) {
//                 var currentOption = document.createElement('option');
//                 currentOption.text = dateArray[i];
//                 selector.appendChild(currentOption);
//     function getDateData(index) {
//             data = listofDates[index]
//             return data
//                 }
//             }
//     function setBubblePlot(chosenDate) {
//             dateindex = listofDates.indexOf(chosenDate);
//              dataForTable = getDateData(dateindex)
//             var trace1 = {
//                 x: Object.keys(dataForTable),
//                 // y: [0, 1, 2],
//                 // x: currentNutrients,
//                 y: Object.values(dataForTable),
//                 mode: 'markers+text',
//                 type: 'bar',
//             };
//             var data = [trace1];
//             var layout = {
//                 title: 'Nutrients',
//                 height: 400,
//                 width: 480
//             };
//         Plotly.newPlot('myDiv', data, layout);
//         }
//         var listofDates = []
//         var listofData = []
//     rows.forEach( data => {
        
//        Object.entries(data).forEach(([key, elem]) =>{
//         listofDates.push(key)
//         listofData.push(elem)
//     })
//     setBubblePlot(listofDates[0])
//     assignOptions(listofDates, dateSelector);
//     var innerContainer = document.querySelector('[data-num="0"'),
//             plotEl = innerContainer.querySelector('.plot'),
//             dateSelector = innerContainer.querySelector('.datelist'); 
        
//         function updateDate(){
//             setBubblePlot(dateSelector.value, listofDates);
//         }
//         dateSelector.addEventListener('change', updateDate, false);
//         })
//     }
//     });

Plotly.d3.json('/nutrient_per_order', function(err, rows){

    function unpack(rows, key) {
        return rows.map(function(row) { return row[key]; });
    }

    var allDates = unpack(rows, 'date'),
        allCalories = unpack(rows, 'total_calories'),
        allFat = unpack(rows, 'total_fat'),
        allCarbs = unpack(rows, 'total_carbs'),
        allFiber = unpack(rows, 'total_fiber'),
        allProtein = unpack(rows, 'total_protein'),
        listofDates = [],
        currentCountry,
        currentCalories = [],
        currentFat = [],
        currentCarbs = [],
        currentFiber = [],
        currentProtein = [];
    for (var i = 0; i < allDates.length; i++ ){
        if (listofDates.indexOf(allDates[i]) === -1 ){
            listofDates.push(allDates[i]);
        }
    }

    function getDateData(currentDate) {
        currentCalories = [],
        currentFat = [],
        currentCarbs = [],
        currentFiber = [],
        currentProtein = [];
        for (var i = 0 ; i < allDates.length ; i++){
            if ( allDates[i] === currentDate ) {
                currentCalories.push(allCalories[i])
                currentFat.push(allFat[i]);
                currentCarbs.push(allCarbs[i]);
                currentFiber.push(allFiber[i]);
                currentProtein.push(allProtein[i]);
                
            }
        }
    };

    // Default Country Data
    setBubblePlot(allDates[0]);

    function setBubblePlot(currentDate) {
        getDateData(currentDate);
        console.log([currentCalories[0],  currentFat[0], currentCarbs[0], currentFiber[0], currentProtein[0]])

        var trace1 = {
            x: ['Fat', 'Carbs', 'Fiber', 'Protein'],
            y: [currentFat[0], currentCarbs[0], currentFiber[0], currentProtein[0]],
            type: 'bar',
            marker:{ color: ['gold', 'pink', 'lightgreen', 'lightpurle'] },
            
        };

        var data = [trace1];

        var layout = {
            height: 400,
            width: 480,
            annotations: [{
                text: 'Calories: ' + currentCalories[0],
                align: 'center',
                valign:'top',
                bordercolor:'darkgray',
                borderpad: 2,
                font :{
                    family: 'Arial',
                    size: 22
                },
                y : 75,
                x: 'paper'


            }]
        };

        Plotly.newPlot('nutrientPlot', data, layout);
    };

    var innerContainer = document.querySelector('[data-num="0"'),
        plotEl = innerContainer.querySelector('.plot'),
        dateSelector = innerContainer.querySelector('.dateOptions');

    function assignOptions(textArray, selector) {
        for (var i = 0; i < textArray.length;  i++) {
            var currentOption = document.createElement('option');
            currentOption.text = textArray[i];
            selector.appendChild(currentOption);
        }
    }

    assignOptions(listofDates, dateSelector);

    function updateDate(){
        setBubblePlot(dateSelector.value);
    }

    dateSelector.addEventListener('change', updateDate, false);
});