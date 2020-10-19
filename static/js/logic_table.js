d3.json("/api/v1.0/parkdata")
  .then(function (data) {
    console.log(data);
    // Do some error handling.
    function tabulate(data, columns) {
      var table = d3.select("table");
      var thead = table.select("thead");
      var tbody = table.select("tbody");

      // append the header row
      thead
        .append("tr")
        .selectAll("th")
        .data(columns)
        .enter()
        .append("th")
        .text(function (column) {
          return column;
        });

      // create a row for each object in the data
      var rows = tbody.selectAll("tr").data(data).enter().append("tr");

      // create a cell in each row for each column
      var cells = rows
        .selectAll("td")
        .data(function (row) {
          return columns.map(function (column) {
            return { column: column, value: row[column] };
          });
        })
        .enter()
        .append("td")
        .text(function (d) {
          return d.value;
        });

      return table;
    }
    // render the table(s)
    tabulate(data, [
      "ParkCode",
      "ParkName",
      "State",
      "Acres",
      "Latitude",
      "Longitude",
    ]);

    // Do some error handling.
  })
  .catch(function (error) {
    // Do some error handling.
  });
