// var data = "../../data/data.json";

var myMap = L.map("map", {
  center: [45.52, -122.67],
  zoom: 6,
});

L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);








d3.json("/api/v1.0/parks")
  .then(function(data) {
    console.log(data)  })
  .catch(function(error) {
    // Do some error handling.
  });


// d3.json("../../data/data.json").then((data) => {
//     console.log(data)
// });
// var data = require("../public/parks.json");
// console.log(data);