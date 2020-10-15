var data = "../data/new.json";
d3.json(data, function (response) {
  //  Create the Traces

  var trace1 = {
    x: response.id,
    y: response.msaid15,
    type: "scatter",
  };

  // Create the data array for the plot
  var data = [trace1];

  // Define the plot layout
  var layout = {
    title: "Square Root of Cancer Survival by Organ",
    xaxis: { title: "Organ" },
    yaxis: { title: "Square Root of Survival" },
  };

  // Plot the chart to a div tag with id "plot"
  Plotly.newPlot("plot", data, layout);
});
