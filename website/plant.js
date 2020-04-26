var config = {
  apiKey: "AIzaSyBd_kch98kROmezUb8AUZVetBZBTkk4LgI",
  authDomain: "earthxhack-2020.firebaseapp.com",
  databaseURL: "https://earthxhack-2020.firebaseio.com",
  projectId: "earthxhack-2020",
  storageBucket: "earthxhack-2020.appspot.com",
  messagingSenderId: "479859258980",
  appId: "1:479859258980:web:54f351fec0ef4731415171",
};

firebase.initializeApp(config);

function addRowHandlers() {
  var table = document.getElementById("dataTab");
  var rows = table.getElementsByTagName("tr");
  for (i = 0; i < rows.length; i++) {
    var currentRow = table.rows[i];
    var createClickHandler = function (row) {
      return function () {
        var cell = row.getElementsByTagName("td")[0];
        var id = cell.innerHTML;
        alert("id:" + id);
      };
    };

    currentRow.onclick = createClickHandler(currentRow);
  }
}
window.onload = addRowHandlers();

function getData() {
  var db = firebase.firestore();
  db.collection("metrics")
    .get()
    .then((querySnapshot) => {
      querySnapshot.forEach((doc) => {
        labels.push(doc.data().label.toString());
        values.push(doc.data().value);
      });
      chart.update();
    });
}

var labels = [];
var values = [];
var planthealth = [];

function getData() {
  var db = firebase.firestore();
  db.collection("metrics")
    .get()
    .then((querySnapshot) => {
      querySnapshot.forEach((doc) => {
        labels.push(doc.data().label.toString());
        values.push(doc.data().value);
      });
      chart.update();
    });
}

function getData(plantnum) {
    db.collection("metrics").get().then((querySnapshot) => {
        querySnapshot.forEach((doc) => {
            labels.push((doc.data().label).toString());
            values.push(doc.data().value);
        });
        chart.update();
    });
}


window.addEventListener("load", getData());

var ctx = document.getElementById("myChart").getContext("2d");
var chart = new Chart(ctx, {
  // The type of chart we want to create
  type: "line",

  // The data for our dataset
  data: {
    labels: labels,
    datasets: [
      {
        data: values,
        label: "Health/Day",
        backgroundColor: "rgb(26, 188, 156)",
        borderColor: "rgb(26, 188, 156)",
      },
    ],
  },

  // Configuration options go here
  options: {
    title: {
      display: true,
      text: "Plant Dataset",
    },
  },
});
