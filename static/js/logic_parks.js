// var data = "../../data/data.json";
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