
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

function thefilter(data, key, x_start, x_end){
    var result = data.filter(el=>new Date(el.order_date)>=x_start && new Date(el.order_date)<=x_end);


    return result;
};

function getArrays(result){
    list1=[]    
        result.forEach(element => 
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
    return [dateList, totalsList]
};

function currencyFormat(num) {
    return '$' + num.toFixed(2).replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1,')
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
   
    var thedata = [{
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
            }
    
            }


let x_end=new Date(Math.max.apply(null, dateList))
let x_start=new Date(Math.min.apply(null, dateList))

console.log(x_start)
console.log(x_end)

let result=thefilter(data, 'order_date', x_start, x_end)
let values=getArrays(result)
thedateList=values[0]
thetotalsList=values[1]
let totalSpending=currencyFormat(thetotalsList.reduce((a,b) => a + b, 0));
let maximumOrderTotal=currencyFormat(Math.max(...thetotalsList));
let minimumOrderTotal=currencyFormat(Math.min(...thetotalsList));
let aveOrderTotal = currencyFormat(thetotalsList.reduce((a,b) => a + b, 0) / thetotalsList.length)
d3.select("#num1").text(totalSpending);
d3.select("#num2").text(maximumOrderTotal);
d3.select("#num3").text(minimumOrderTotal);
d3.select("#num4").text(aveOrderTotal);
            
Plotly.newPlot('budget_analysis', thedata, layout)

budget_analysis.on('plotly_relayout',function(eventdata){  
x_start = new Date(eventdata['xaxis.range'][0])
x_end = new Date(eventdata['xaxis.range'][1])

console.log(x_start+"----"+x_end)

result=thefilter(data, 'order_date', x_start, x_end)
values=getArrays(result)
thedateList=values[0]
thetotalsList=values[1]
totalSpending=currencyFormat(thetotalsList.reduce((a,b) => a + b, 0));
maximumOrderTotal=currencyFormat(Math.max(...thetotalsList));
minimumOrderTotal=currencyFormat(Math.min(...thetotalsList));
aveOrderTotal = currencyFormat(thetotalsList.reduce((a,b) => a + b, 0) / thetotalsList.length)
d3.select("#num1").text(totalSpending);
d3.select("#num2").text(maximumOrderTotal);
d3.select("#num3").text(minimumOrderTotal);
d3.select("#num4").text(aveOrderTotal);


  })
})
}

getData()



