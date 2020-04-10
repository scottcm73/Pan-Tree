
function getDistinct(items, key){
    var lookup = {};
  
    var result = [];

    for (var item, i = 0; item = items[i++];) {
        let name = item[key];

    if (!(name in lookup)) {
        lookup[name] = 1;
        result.push(name);
        }
    }
    return result;

};
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

        console.log(element)

    });
    dateList=[]
    totalsList=[]
    Object.entries(sumDict).forEach(([date, total])=>{

        dateList.push(date);
        totalsList.push(total);

    });
    let datestrArray=getDistinct(data, 'order_date')
    
    var data = [
        {
          x: dateList,
          y: totalsList,
          type: 'bar'
        }
      ];
      Plotly.newPlot('budget_analysis', data);
    
})
};

getData();

