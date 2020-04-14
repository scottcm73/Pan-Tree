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

function onlyUnique(value, index, self) { 
    return self.indexOf(value) === index;
}

function getData(){
    d3.json('/budget_data').then((data) => 
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
            Object.entries(sumDict).forEach(([date, total])=>
            {   
                   
                dateList.push(new Date(date));
               
                
                // usage example:
                
                //var unique = dateList.filter(onlyUnique);
                totalsList.push(total)
                })
   var data = [{
        type: 'bar',
        x: dateList,
        y: totalsList
    }]
    var layout = {
        title: 'Budget Analysis',
        xaxis: {
                rangeselector: selectorOptions,
                rangeslider: {}
            },
           
            yaxis: {
                fixedrange: true
                title: {
                  text: 'y Axis',
                  font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                  }
                }
              }
            }
Plotly.plot('budget_analysis', data, layout)

})
}

getData()
