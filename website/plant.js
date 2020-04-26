var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ['1', '2', '3', '4', '5'],
        datasets: [{
            label: 'Plant dataset',
            backgroundColor: 'rgb(26, 188, 156)',
            borderColor: 'rgb(26, 188, 156)',
            data: [0, 15, 10, 20, 30]
        }]
    },

    // Configuration options go here
    options: {}
});