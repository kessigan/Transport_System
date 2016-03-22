// AmCharts.makeChart(div, data);

var map = AmCharts.makeChart( "chartdiv", {
  type: "map",
  "theme": "none",

  colorSteps: 10,

  dataProvider: {
    map: "southAfricaLow",
    areas: [ {
      id: "LS",
      value: 4447100
    }, {
      id: "ZA-EC",
      value: 626932
    }, {
      id: "ZA-FS",
      value: 5130632
    }, {
      id: "ZA-GT",
      value: 2673400
    }, {
      id: "ZA-LP",
      value: 33871648
    }, {
      id: "ZA-MP",
      value: 4301261
    }, {
      id: "ZA-NC",
      value: 3405565
    }, {
      id: "ZA-NL",
      value: 783600
    }, {
      id: "ZA-MP",
      value: 15982378
    }, {
      id: "ZA-NC",
      value: 8186453
    }, {
      id: "ZA-NL",
      value: 1211537
    }, {
      id: "ZA-NW",
      value: 1293953
    }, {
      id: "ZA-WC",
      value: 12419293
    } ]
  },

  areasSettings: {
    autoZoom: true
  },

  valueLegend: {
    right: 10,
    minValue: "little",
    maxValue: "a lot!"
  },

  "export": {
    "enabled": true
  }

} );
  
  map.setpathToImages = "../imag/";