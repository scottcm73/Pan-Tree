const table = d3.select('#inventory_table')
const tableHead = d3.select('#table_header')
const headRow = tableHead.append('tr')
const tableBody = d3.select('#table_body')

function makeTableHeader() {
    headRow.html('')
    d3.json('/table_data').then( function(data) {
        Object.keys(data[0]).forEach(function(item) {
            // if (item == 'Date' || item == 'Product' || item == 'Amount Bought' || item == 'Amount Left') {
                const headItem = headRow.append('th')
                headItem.text(item)
            // }
        
        })
    // const headItem = headRow.append('th')
    // headItem.text('Actions')
})
}
            

function makeTableBody() {
    tableBody.html('')
    //load in data from backend route 
    d3.json('/table_data').then( function(data) {
        data.forEach( dict => {
            tableRow = tableBody.append('tr')
            Object.entries(dict).forEach(([key, item]) => {
                // if (key == 'Date' || key == 'Product' || key == 'Amount Bought' || key == 'Amount Left') {
                    const tableValue = tableRow.append('td')
                    tableValue.text(item)
// }
        })
        // const appendButton = tableRow.append('td')
        // appendButton.append('button').attr('id', dict['order_id'] + ' ' + dict['Product']).text('Cook')
        // appendButton.append('button').attr('id', dict['order_id'] + ' ' + dict['Product']).text('Trash')
    })
})
}

makeTableHeader()
makeTableBody()
