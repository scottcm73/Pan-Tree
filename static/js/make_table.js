//declaration of variables selected from template
const table = d3.select('#inventory_table')
const tableHead = d3.select('#table_header')
const headRow = tableHead.append('tr')
const tableBody = d3.select('#table_body')

function makeTableHeader() {
    // set the html to empty string
    headRow.html('')
    //call in data from flask backend route
    d3.json('/table_data').then( function(data) {
        //reference the first object and make the keys the table header
        Object.keys(data[0]).forEach(function(item) {
            //check that only the needed data is extracted from the query
            if (item == 'Date' || item == 'Product' || item == 'Amount Bought' || item == 'Amount Left') {
                //append the data to the dom 
                const headItem = headRow.append('th')
                headItem.text(item)
            }
        
        })
    //append button column
    const headItem = headRow.append('th')
    headItem.text('Actions')
})
}
            

function makeTableBody() {
    tableBody.html('')
    //load in data from backend route 
    d3.json('/table_data').then( function(data) {
        data.forEach( dict => {
            // apend a row or every entry
            tableRow = tableBody.append('tr')
            //reference the objects
            Object.entries(dict).forEach(([key, item]) => {
                //check that only the needed data is extracted from the query
                if (key == 'Date' || key == 'Product' || key == 'Amount Bought' || key == 'Amount Left') {
                    //append the data to the dom 
                    const tableValue = tableRow.append('td')
                    tableValue.text(item)
}
        })
        //add buttons to the column with respective id
        const appendButton = tableRow.append('td')
        var cookButton = appendButton.append('button')
            .text('Cook')
            .on("click", function() {
                window.open('/cook_buttons/' + dict['order_id'] + '/' + dict['product_id'])
            })
        var trashButton = appendButton.append('button')
            .text('Trash')
            .on("click", function() {
                window.open('/trash_buttons/' + dict['order_id'] + '/' + dict['product_id'])
            })
    })
})
}
//cal the functions
makeTableHeader()
makeTableBody()
