const table = d3.select('#inventory_table')
const tableHead = d3.select('#table_header')
const headRow = tableHead.append('tr')

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
    headItem.text('Cook')
    const headItem2 = headRow.append('th')
    headItem2.text('Trash')


})
}


makeTableHeader()

d3.json('/table_data').then( function(data) {

    function cookReDirect(event) {
        window.location.replace('/cook_buttons/' + event.data['order_id'] + '/' + event.data['product_id'])
    }
    function trashReDirect(event) {
        window.location.replace('/trash_buttons/' + event.data['order_id'] + '/' + event.data['product_id'])
      
    }
        var table = $('#inventory_table').DataTable( {
        data: data,
        columns: [
            { data: 'Date' },
            { data: 'Product' },
            { data: 'Amount Bought' },
            { data: 'Amount Left' },
            {
                name: "Cook Button",
                searchable: false,
                title: "Use Item",
                orderable: false,
                defaultContent: "<input type=\"button\" value=\"Enjoy!\"> ",
                createdCell: function(cell, cellData, rowData, rowIndex, colIndex) {
                  $(cell).on("click", "input", rowData, cookReDirect);
                }
              },
              {
                name: "trashButton",
                searchable: false,
                title: "Trash Item",
                orderable: false,
                defaultContent: "<input type=\"button\" value=\"not enjoyed\"> ",
                createdCell: function(cell, cellData, rowData, rowIndex, colIndex) {
                  $(cell).on("click", "input", rowData, trashReDirect);
                }
              }
             ]
    })

    })