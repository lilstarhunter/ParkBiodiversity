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
