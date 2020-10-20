const mapOne = L.map('mapOne', {
  
}).setView([45.52, -122.67], 3);

const mapTwo = L.map('mapTwo', {
  
}).setView([45.52, -122.67], 3);

const mapThree = L.map('mapThree', {
  
}).setView([45.52, -122.67], 3);

// Add a tile layer to the map (Mapbox Streets tile layer)
const mapboxToken = 'pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';
const mapboxUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={token}';
const mapboxAttribution = [
  'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors,',
  '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>,',
  'Imagery © <a href="http://mapbox.com">Mapbox</a>',
].join(" ");

const mapbox = (map) => {
  return L.tileLayer(mapboxUrl, {
    id: 'mapbox.streets',
    token: mapboxToken,
    attribution: mapboxAttribution,
  }).addTo(map)
};

[mapOne, mapTwo, mapThree].forEach(mapInstance => mapbox(mapInstance));


d3.json("/api/v1.0/animal_biodiv")
    .then(function (data) {
      // console.log(data);


      // Mammal marker group
      var mammalMarkers = []
        data.forEach((d) => {
          if(d.Category === "Mammal"){
            let options = {
              radius: (d["Biodiversity Count"]/50),
              fillColor: 'brown',
              color: "black",
              weight: 1,
              opacity: 1,
              fillOpacity: 0.6
            }

            mammalMarkers.push(L.circleMarker([d.lat, d.lon], options)
              .bindPopup(`<h3>${d['Park Name']}</h3><h4>Biodiversity Count: ${d["Biodiversity Count"]}`))
          };
        });

        var mammalLayer = L.layerGroup(mammalMarkers) 


          // fish layer group
        var fishMarkers = []
        data.forEach((d) => {
          if(d.Category === "Fish"){
            let options = {
              radius: (d["Biodiversity Count"]/50),
              fillColor: 'blue',
              color: "black",
              weight: 1,
              opacity: 1,
              fillOpacity: 0.6
            }

            fishMarkers.push(L.circleMarker([d.lat, d.lon], options)
              .bindPopup(`<h3>${d['Park Name']}</h3><h4>Biodiversity Count: ${d["Biodiversity Count"]}`))
          };
        });
        var fishLayer = L.layerGroup(fishMarkers) 



        // Amphibian layer group
        var amphibianMarkers = []
        data.forEach((d) => {
          if(d.Category === "Amphibian"){
            let options = {
              radius: (d["Biodiversity Count"]/50),
              fillColor: 'green',
              color: "black",
              weight: 1,
              opacity: 1,
              fillOpacity: 0.6
            }

            amphibianMarkers.push(L.circleMarker([d.lat, d.lon], options)
              .bindPopup(`<h3>${d['Park Name']}</h3><h4>Biodiversity Count: ${d["Biodiversity Count"]}`))
          };
        });
        var amphibianLayer = L.layerGroup(amphibianMarkers)



        // Bird layer group
        var birdMarkers = []
        data.forEach((d) => {
          if(d.Category === "Bird"){
            let options = {
              radius: (d["Biodiversity Count"]/50),
              fillColor: 'purple',
              color: "black",
              weight: 1,
              opacity: 1,
              fillOpacity: 0.6
            }

            birdMarkers.push(L.circleMarker([d.lat, d.lon], options)
              .bindPopup(`<h3>${d['Park Name']}</h3><h4>Biodiversity Count: ${d["Biodiversity Count"]}`))
          };
        });
        var birdLayer = L.layerGroup(birdMarkers)



        // Invertebrate layer group
        var invertebrateMarkers = []
        data.forEach((d) => {
          if(d.Category === "Invertebrate"){
            let options = {
              radius: (d["Biodiversity Count"]/50),
              fillColor: 'yellow',
              color: "black",
              weight: 1,
              opacity: 1,
              fillOpacity: 0.6
            }

            invertebrateMarkers.push(L.circleMarker([d.lat, d.lon], options)
              .bindPopup(`<h3>${d['Park Name']}</h3><h4>Biodiversity Count: ${d["Biodiversity Count"]}`))
          };
        });
        var invertebrateLayer = L.layerGroup(invertebrateMarkers)

        var overlayMaps = {
          Mammals: mammalLayer,
          Fish: fishLayer,
          Amphibian: amphibianLayer,
          Birds: birdLayer,
          Invertebrate: invertebrateLayer
        };
        L.control.layers(overlayMaps).addTo(mapOne);
    })
    .catch(function (error) {
      // Do some error handling.
    });

// =============================================================
//         Plant Map
// =============================================================



d3.json("/api/v1.0/plant_biodiv")
    .then(function (data) {
      console.log(data);
      var cat = []

      data.forEach(d =>{
        
        if (cat.includes(d.Category)){
      
        }else{
          cat.push(d.Category)
        }
      })
      console.log(cat)


      // Mammal marker group
      var vascularplantMarkers = []
        data.forEach((d) => {
          if(d.Category === "Vascular Plant"){
            let options = {
              radius: (d["Biodiversity Count"]/50),
              fillColor: 'brown',
              color: "black",
              weight: 1,
              opacity: 1,
              fillOpacity: 0.6
            }

            vascularplantMarkers.push(L.circleMarker([d.lat, d.lon], options)
              .bindPopup(`<h3>${d['Park Name']}</h3><h4>Biodiversity Count: ${d["Biodiversity Count"]}`))
          };
        });

        var vascularplantLayer = L.layerGroup(vascularplantMarkers) 

        var nonvascularplantMarkers = []
        data.forEach((d) => {
          if(d.Category === "Nonvascular Plant"){
            let options = {
              radius: (d["Biodiversity Count"]/50),
              fillColor: 'green',
              color: "black",
              weight: 1,
              opacity: 1,
              fillOpacity: 0.6
            }

            nonvascularplantMarkers.push(L.circleMarker([d.lat, d.lon], options)
              .bindPopup(`<h3>${d['Park Name']}</h3><h4>Biodiversity Count: ${d["Biodiversity Count"]}`))
          };
        });

        var nonvascularplantLayer = L.layerGroup(nonvascularplantMarkers) 



        

        var overlayMaps2 = {
          VascularPlant: vascularplantLayer,
          NonnascularPlant: nonvascularplantLayer
        };
        L.control.layers(overlayMaps2).addTo(mapTwo);
    })
    .catch(function (error) {
      // Do some error handling.
      console.log(error)
    });