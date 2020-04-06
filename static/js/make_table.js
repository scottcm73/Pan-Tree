const table = d3.select('#inventory_table')
const tableHead = d3.select('#table_header')
const headRow = tableHead.append('tr')
const tableBody = d3.select('#table_body')




//Promise.all([])
function makeTableHeader() {
    headRow.html('')
    order_data = []
    //load in data from backend route 
    d3.json('/order_data/1').then( function(data) {
        Object.keys(data[0]).forEach(function(item) {
            console.log(item)
            const headItem = headRow.append('th')
            headItem.text(item)
        })
        }
        )
    } 
function makeTableBody() {
    headRow.html('')
    order_data = []
    //load in data from backend route 
    d3.json('/order_data/1').then( function(data) {
        data.forEach( dict => {
        tableRow = tableBody.append('tr')
        Object.values(dict).forEach(function(item) {
            console.log(item)
            const tableValue = tableRow.append('td')
            tableValue.text(item)
        })
    }
)}
)} 
    

makeTableHeader()
makeTableBody()
