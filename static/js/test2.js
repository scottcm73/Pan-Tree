
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



d3.json('/dashboard-data').then((items) => {
    let datestrArray=getDistinct(items, 'order_date')

    datestrArray.sort(function(a,b){
        return new Date(a) - new Date(b)
      })
    for (index = 0; index < datestrArray.length; index++) { 
        
    
        var newArray = items.filter(function (el) {
        return el.order_date === datestrArray[index] 

      
        });
       
    } 
    console.log(newArray)

    


});

    

    
    


   