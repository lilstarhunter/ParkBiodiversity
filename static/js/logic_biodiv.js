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

// INSERT CLICK EVENT FOR DROP DOWN MENU
function animal(data) {
  d3.json("/api/v1.0/animal_biodiv")
    .then(function (data) {
      console.log(data);
      data.forEach((d) => {
        L.marker([d.ParkName, d.Category])
          .bindPopup(`<h3>${d.ParkName}</h3>`)
          .addTo(myMap);
      });
    })
    .catch(function (error) {
      // Do some error handling.
    });
}

// INSERT CLICK EVENT FOR DROP DOWN MENU
function plant(data) {
  d3.json("/api/v1.0/plant_biodiv")
    .then(function (data) {
      console.log(data);
      data.forEach((d) => {
        L.marker([d.ParkName, d.Category])
          .bindPopup(`<h3>${d.ParkName}</h3>`)
          .addTo(myMap);
      });
    })
    .catch(function (error) {
      // Do some error handling.
    });
}

// INSERT CLICK EVENT FOR DROP DOWN MENU
function insect(data) {
  d3.json("/api/v1.0/insect_biodiv")
    .then(function (data) {
      console.log(data);
      data.forEach((d) => {
        L.marker([d.ParkName, d.Category])
          .bindPopup(`<h3>${d.ParkName}</h3>`)
          .addTo(myMap);
      });
    })
    .catch(function (error) {
      // Do some error handling.
    });
}

// INSERT CLICK EVENT FOR DROP DOWN MENU
function fungi(data) {
  d3.json("/api/v1.0/fungi_biodiv")
    .then(function (data) {
      console.log(data);
      data.forEach((d) => {
        L.marker([d.ParkName, d.Category])
          .bindPopup(`<h3>${d.ParkName}</h3>`)
          .addTo(myMap);
      });
    })
    .catch(function (error) {
      // Do some error handling.
    });
}
