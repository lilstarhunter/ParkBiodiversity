d3.json("http://127.0.0.1:5000/api/v1.0/survivors").then((data) => {
  //  Create the Traces
  // data = object.assign(data1)
  // var data = Object.assign({}, data1)

  console.log(data)
  var trace1 = {
    x: data.organ,
    y: data.survival,
    type: "box",
    name: "Cancer Survival",
    boxpoints: "all"
  };

  // Create the data array for the plot
  var data = [trace1];
localStorage
  // Define the plot layout
  var layout = {
    title: "Square Root of Cancer Survival by Organ",
    xaxis: { title: "Organ" },
    yaxis: { title: "Square Root of Survival" }
  };

  // Plot the chart to a div tag with id "plot"
  Plotly.newPlot("plot", data, layout);
});
