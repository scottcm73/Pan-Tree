
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

    
    var data = [
        {
          x: dateList,
          y: totalsList,
          type: 'bar'
        }
      ];

      $(function() {

        var start = moment().subtract(29, 'days');
        var end = moment();
    
        function cb(start, end) {
            $('#reportrange span').html(start.format('MMMM D, YYYY') + ' - ' + end.format('MMMM D, YYYY'));
        }
    
        $('#reportrange').daterangepicker({
            startDate: start,
            endDate: end
           
        }, cb);
    
        cb(start, end);
    
    });
   

      Plotly.newPlot('budget_analysis', data);
    
    
})
};
$('#reportrange').on('apply.daterangepicker', function(ev, picker) {
    console.log(picker.startDate.format('YYYY-MM-DD'));
    console.log(picker.endDate.format('YYYY-MM-DD'));
    let myHeader = ["order_date", "total"];
    let mydata = [myHeader];
    
for(i=0; i<dateList.length(); i++)
{
    mydata.push([myCol1[i],myCol2[i]]);
}
x=0

function startEndFilter(mydata, x){
let start = new Date(mydata[0].min);
let end   = new Date(mydata[1].max);

return items.filter(item => {
   let date = new Date(item.created_at);
   return date >= start && date <= end;
                            });  
                        
                        }; 


getData();
     




    


   