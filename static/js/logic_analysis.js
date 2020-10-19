//=========Define SVG Area and Margins=========//
//Define SVG area dimensions
var svgWidth = 800;
var svgHeight = 600;
//Define chart's margins as an object
var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100,
};
// Define dimensions of the chart area
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Append the SVG object to the body of the page
var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight + 40); //extra padding for third label

// Append a chart group
var chartGroup = svg
  .append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`)
  .attr("class", "chart");

d3.json("/api/v1.0/analysis").then(function (data) {
  data.forEach((d) => {
    var xScale = d3
      .scaleLinear()
      .domain(d3.extent(data, (d) => d.acres))
      .range([0, width]);
    var yScale = d3
      .scaleLinear()
      .domain(d3.extent(data, (d) => d.count))
      .range([height, 0]);

    // create axes
    var xAxis = d3.axisBottom(xScale);
    var yAxis = d3.axisLeft(yScale);

    // append axes
    chartGroup
      .append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(xAxis);
    chartGroup.append("g").call(yAxis);

    //Create a circles group
    var circlesGroup = chartGroup
      .selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", (d) => xScale(d.acres))
      .attr("cy", (d) => yScale(d.count))
      .attr("r", "15")
      .attr("stroke-width", "1");

    var circleLabels = chartGroup
      .selectAll(null)
      .data(data)
      .enter()
      .append("text");

    circleLabels
      .attr("x", function (d) {
        return xScale(d.acres);
      })
      .attr("y", function (d) {
        return yScale(d.count);
      })
      .text(function (d) {
        return d.state;
      });

    chartGroup
      .selectAll("text")
      .data(data)
      .enter()
      .append("text")
      .attr("x", (d) => xScale(d.acres))
      .attr("y", (d) => yScale(d.count));

    chartGroup
      .append("text")
      .attr("transform", `translate(500, 500)`)
      .text("Park Acres");
    chartGroup
      .append("text")
      .attr("transform", `translate(-35, 200)rotate(270)`)
      .text("Biodiversity");
  });

  // data.forEach(function (data) {

  // });
});
// // INSERT CLICK EVENT FOR DROP DOWN MENU
// function animal(data) {
//   d3.json("/api/v1.0/animal_biodiv")
//     .then(function (data) {
//       console.log(data);
//       data.forEach((d) => {
//         L.marker([d.ParkName, d.Category])
//           .bindPopup(`<h3>${d.ParkName}</h3>`)
//           .addTo(myMap);
//       });
//     })
//     .catch(function (error) {
//       // Do some error handling.
//     });
// }

// // INSERT CLICK EVENT FOR DROP DOWN MENU
// function plant(data) {
//   d3.json("/api/v1.0/plant_biodiv")
//     .then(function (data) {
//       console.log(data);
//       data.forEach((d) => {
//         L.marker([d.ParkName, d.Category])
//           .bindPopup(`<h3>${d.ParkName}</h3>`)
//           .addTo(myMap);
//       });
//     })
//     .catch(function (error) {
//       // Do some error handling.
//     });
// }

// // INSERT CLICK EVENT FOR DROP DOWN MENU
// function insect(data) {
//   d3.json("/api/v1.0/insect_biodiv")
//     .then(function (data) {
//       console.log(data);
//       data.forEach((d) => {
//         L.marker([d.ParkName, d.Category])
//           .bindPopup(`<h3>${d.ParkName}</h3>`)
//           .addTo(myMap);
//       });
//     })
//     .catch(function (error) {
//       // Do some error handling.
//     });
// }

// // INSERT CLICK EVENT FOR DROP DOWN MENU
// function fungi(data) {
//   d3.json("/api/v1.0/fungi_biodiv")
//     .then(function (data) {
//       console.log(data);
//       data.forEach((d) => {
//         L.marker([d.ParkName, d.Category])
//           .bindPopup(`<h3>${d.ParkName}</h3>`)
//           .addTo(myMap);
//       });
//     })
//     .catch(function (error) {
//       // Do some error handling.
//     });
// }
