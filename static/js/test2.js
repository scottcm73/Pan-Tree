
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
// function getTotal(data, key){
//     var total = 0,  //set a variable that holds our total
//     thetotal = data,  //reference the element in the "JSON" aka object literal we want
//     i;
//     for (i = 0; i < thetotal.length; i++) {  //loop through the array
//         total += thetotal[i][key];  //Do the math!
// }
//     return total
// };
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
    
        if (!(element[0] in sumDict)) 
        { 
            sumDict[element[0] = element[1]]
          
        }
        else if(!(element[0] in sumDict)) 
        { 
            sumDict[element[0]]+= element[1]

        }

    });
    console.log(sumDict)
    console.log(list1)
    let datestrArray=getDistinct(data, 'order_date')

    datestrArray.sort(function(a,b){
        return new Date(a) - new Date(b)
    })
   
})
};

getData();


    
    


   