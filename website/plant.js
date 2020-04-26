var config = {
    apiKey: "AIzaSyBd_kch98kROmezUb8AUZVetBZBTkk4LgI",
    authDomain: "earthxhack-2020.firebaseapp.com",
    databaseURL: "https://earthxhack-2020.firebaseio.com",
    projectId: "earthxhack-2020",
    storageBucket: "earthxhack-2020.appspot.com",
    messagingSenderId: "479859258980",
    appId: "1:479859258980:web:54f351fec0ef4731415171"
};

firebase.initializeApp(config);

var labels = [];
var values = [];

function getData() {
    console.log("getData Invoked");
    var db = firebase.firestore();
    db.collection("metrics").get().then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            labels.push(doc.data().label);
            values.push(doc.data().value);
            console.log(doc.data())
        });
        chart.update();
    });
}

window.addEventListener("load", getData());

var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: labels,
        datasets: [{
            label: 'Plant dataset',
            backgroundColor: 'rgb(26, 188, 156)',
            borderColor: 'rgb(26, 188, 156)',
            data: values
        }]
    },

    // Configuration options go here
    options: {}
});