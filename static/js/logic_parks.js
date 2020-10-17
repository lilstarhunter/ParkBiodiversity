// var data = "../../data/data.json";
d3.json("/api/v1.0/parks", function (response) {
  console.log(response);
});

// d3.json("../../data/data.json").then((data) => {
//     console.log(data)
// });
// var data = require("../public/parks.json");
// console.log(data);