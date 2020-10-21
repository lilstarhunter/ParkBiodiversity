var myMap = L.map("map", {
  center: [40.52, -122.67],
  zoom: 4.5,
});

L.tileLayer(
  "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
  {
    attribution:
      "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY,
  }
).addTo(myMap);

// global variable for park data
var parkData = [];

// Grab data and assign to global variable
d3.json("/api/v1.0/parkdata")
  .then(function (data) {
    parkData = data;

    data.forEach((d) => {
      let options = {
        radius: d.Acres / 200000,
        fillColor: "blue",
        color: "black",
        weight: 1,
        opacity: 1,
        fillOpacity: 0.6,
      };
      L.circleMarker([d.Latitude, d.Longitude], options)
        .bindPopup(`<h3>${d.ParkName}</h3>`)
        .addTo(myMap);
    });
    // Creating the drop down menu
    data.forEach((d) => {
      var dropdown = d3.select("#selDataset");
      dropdown.append("option").text(d.ParkName).property("value");
    });
    parkInfo();
  })

  .catch(function (error) {
    // Do some error handling.
  });

function parkInfo() {
  selectValue = d3.select("select").property("value");
  var result = parkData.filter((d) => d.ParkName === selectValue)[0];
  var info = d3.select("#state-info");

  info.html("");

  Object.entries(result).forEach((i) => {
    info.append("h5").text(i[0] + ": " + i[1] + "\n");
  });
}

var mergeData = [];
d3.json("/api/v1.0/analysis").then(function (data) {
  mergeData = data;
  var homeResult = mergeData.filter((d) => d.ParkName === selectValue)[0];
  // Grab variables from graphing
  var categoryLabel = homeResult.Category;
  var categoryValue = homeResult.BiodiversityCount;

  var trace = {
    x: categoryLabel,
    y: categoryValue,
    type: "bar",
  };

  var chartData = [trace];
  var layout = {
    color : ['#f3cec9', '#e7a4b6', '#cd7eaf', '#a262a9', '#6f4d96', '#3d3b72'],
    yaxis: {
      type: "Category",
    },
    xaxis: { title: "Biodiversity" },
    title: "Park Biodiversity",
  };
  // console.log(result);
  Plotly.newPlot("bar", chartData, layout);

  histogram();
  // console.log(mergeData);
});

function histogram() {
  selectValue = d3.select("select").property("value");
  var result = mergeData.filter((d) => d.ParkName === selectValue);
  // Grab variables from graphing
  var categoryLabel = result.map((i) => i.Category);
  var categoryValue = result.map((i) => i.BiodiversityCount);

  var trace = {
    x: categoryValue,
    y: categoryLabel,
    type: "bar",
    orientation: "h",
  };

  var chartData = [trace];
  var layout = {
    yaxis: {
      type: "category",
    },
    xaxis: { title: "Category" },
    title: "Park Biodiversity",
  };
  // console.log(result);
  Plotly.newPlot("bar", chartData, layout);
}

function optionChanged() {
  parkInfo();
  histogram();
}
