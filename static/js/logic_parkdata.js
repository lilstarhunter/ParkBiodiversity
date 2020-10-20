var myMap = L.map("map", {
  center: [45.52, -122.67],
  zoom: 3,
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

function demoInfo(id) {
        d3.json("samples.json").then((data)=> {
            var metadata = data.metadata;
            console.log(metadata)
         var result = metadata.filter(meta => meta.id.toString() === id)[0];
         var demographicInfo = d3.select("#sample-metadata");
        
         demographicInfo.html("");
  
       // inject demographic data for the id and append the info to the panel html
          Object.entries(result).forEach((i) => {   
              demographicInfo.append("h5").text(i[0].toUpperCase() + ": " + i[1] + "\n");    
          });
      });
  }

function optionChanged(id) {
  Plots(id);
  demoInfo(id);
}


d3.json("/api/v1.0/parkdata")
  .then(function (data) {
    console.log(data);
    data.forEach((d) => {
      L.marker([d.Latitude, d.Longitude])
        .bindPopup(`<h3>${d.ParkName}</h3>`)
        .addTo(myMap);
    });
    data.forEach((d) => {
      var dropdown = d3.select("#selDataset");
      dropdown.append("option").text(d.state).property("value");
    });
  })
  .catch(function (error) {
    // Do some error handling.
  });
