function makeplot() {
    Plotly.d3.csv("../Resources/pop_shop_days.csv", function (data) { processData(data) });
};

function processData(allRows) {

    console.log(allRows);
    var x = [], y = [];

    for (var i = 0; i < allRows.length; i++) {
        row = allRows[i];
        x.push(row['order_date']);
        y.push(row['weekday']);
    }
    console.log('X', x, 'Y', y);
    makePlotly(x, y);
}

function makePlotly(x, y) {
    var plotDiv = document.getElementById("plot");
    var traces = [{
        x: x,
        y: y
    }];

    Plotly.newPlot('pop_shop_days', traces,
        { title: 'Most Popular Shopping Days' });
};
makeplot();