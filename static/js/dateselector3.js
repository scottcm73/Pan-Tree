
function onlyUnique(data) { 
    newArray = [];
    for(n in data){
        if(!newArray.indexOf(n)){
            newArray.push(n);
        }
}
}
function getTotal(data, key){
    var total = 0,  //set a variable that holds our total
    thetotal = data,  //reference the element in the "JSON" aka object literal we want
    i;
    for (i = 0; i < thetotal.length; i++) {  //loop through the array
        total += thetotal[i][key];  //Do the math!
}
    return total
};
function getData(){
d3.json('/dashboard-data').then((data) => 
{
    list1=[]    
    data.forEach(element => 
        {let datePrice = [element['order_date'],
        element['price']]
        list1.push(datePrice)

    });
    sumDict={}
    list1.forEach(element =>
    {
    
        if (sumDict.hasOwnProperty( element[0] ) ) {
            sumDict[ element[0] ] = sumDict[ element[0] ] + element[1];
        } else {
            sumDict[ element[0] ] = element[1];
        }

    

    });
    dateList=[]
    totalsList=[]
    Object.entries(sumDict).forEach(([date, total])=>{

        dateList.push(date);
        totalsList.push(total);

    });
    

 
let arrayofArrays=[dateList, totalsList]


return arrayofArrays;
    
})

};
var xField = 'Date';
var yField = 'Total Expenditure';

var selectorOptions = {
    buttons: [{
        step: 'month',
        stepmode: 'backward',
        count: 1,
        label: '1m'
    }, {
        step: 'month',
        stepmode: 'backward',
        count: 6,
        label: '6m'
    }, {
        step: 'year',
        stepmode: 'todate',
        count: 1,
        label: 'YTD'
    }, {
        step: 'year',
        stepmode: 'backward',
        count: 1,
        label: '1y'
    }, {
        step: 'all',
    }],
};



    var data = prepData();
    var layout = {
        title: 'Time series with range slider and selectors',
        xaxis: {
            rangeselector: selectorOptions,
            rangeslider: {}
        },
        yaxis: {
            fixedrange: true
        }
        
    };
Plotly.newPlot("budget_analysis", data, layout);

   


function prepData() {
    
    var totalsList=getData()[0];
    var dateList=getData()[1];
    var uniqueDates = onlyUnique(dateList);
    console.log(totalsList);
    // console.log(uniqueDates);
    return [{
        mode: 'lines',

        x: uniqueDates,
        y: totalsList
    }];
}