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

function getData(callbackIN) {
  var ref = firebase.firestore().ref("plant_health0");
  ref.once("value").then(function (snapshot) {
    callbackIN(snapshot.val());
  });
}

window.addEventListener("load", getData(genFunction));

function genFunction(data) {
  var cdata = [];
  var len = data.length;
  for (var i = 1; i < len; i++) {
    cdata.push({
      label: data[i]["label"],
      value: data[i]["value"],
    });
  }
}

var firebaseChart = new FusionCharts({
    type: "area2d",
    renderAt: "chart-container",
    width: "250",
    height: "150",
    dataFormat: "json",
    dataSource: {
    chart: {
      caption: "Plant Trend",
      subCaption: "Last 1 Day",
      subCaptionFontBold: "0",
      captionFontSize: "20",
      subCaptionFontSize: "17",
      captionPadding: "15",
      captionFontColor: "#8C8C8C",
      baseFontSize: "14",
      baseFont: "Barlow",
      canvasBgAlpha: "0",
      bgColor: "#FFFFFF",
      bgAlpha: "100",
      showBorder: "0",
      showCanvasBorder: "0",
      showPlotBorder: "0",
      showAlternateHGridColor: "0",
      usePlotGradientColor: "0",
      paletteColors: "#6AC1A5",
      showValues: "0",
      divLineAlpha: "5",
      showAxisLines: "1",
      drawAnchors: "0",
      xAxisLineColor: "#8C8C8C",
      xAxisLineThickness: "0.7",
      xAxisLineAlpha: "50",
      yAxisLineColor: "#8C8C8C",
      yAxisLineThickness: "0.7",
      yAxisLineAlpha: "50",
      baseFontColor: "#8C8C8C",
      toolTipBgColor: "#FA8D67",
      toolTipPadding: "10",
      toolTipColor: "#FFFFFF",
      toolTipBorderRadius: "3",
      toolTipBorderAlpha: "0",
      drawCrossLine: "1",
      crossLineColor: "#8C8C8C",
      crossLineAlpha: "60",
      crossLineThickness: "0.7",
      alignCaptionWithCanvas: "1",
    },

    data: cdata,
  },
});

firebaseChart.render();