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

// function demoInfo(id) {
//         d3.json("samples.json").then((data)=> {
//             var metadata = data.metadata;
//             console.log(metadata)
//          var result = metadata.filter(meta => meta.id.toString() === id)[0];
//          var demographicInfo = d3.select("#sample-metadata");

//          demographicInfo.html("");

//        // inject demographic data for the id and append the info to the panel html
//           Object.entries(result).forEach((i) => {
//               demographicInfo.append("h5").text(i[0].toUpperCase() + ": " + i[1] + "\n");
//           });
//     });
// }

// function optionChanged(id) {
//   Plots(id);
//   demoInfo(id);
// }

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
    parkMapMarkers();
  })

  .catch(function (error) {
    // Do some error handling.
  });

function parkMapMarkers() {
  selectValue = d3.select("select").property("value");
  var result = parkData.filter((d) => d.ParkName === selectValue)[0];
  var info = d3.select("#state-info");

  info.html("");

  Object.entries(result).forEach((i) => {
    info.append("h5").text(i[0] + ": " + i[1] + "\n");
  });
}

function optionChanged() {
  parkMapMarkers();
}
