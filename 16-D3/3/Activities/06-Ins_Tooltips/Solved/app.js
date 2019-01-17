// The code for the chart is wrapped inside a function
// that automatically resizes the chart
function makeResponsive() {

  // if the SVG area isn't empty when the browser loads, remove it
  // and replace it with a resized version of the chart
  const svgArea = d3.select("body").select("svg");
  if (!svgArea.empty()) {
    svgArea.remove();
  }

  // SVG wrapper dimensions are determined by the current width
  // and height of the browser window.
  const svgWidth = window.innerWidth;
  const svgHeight = window.innerHeight;

  const margin = {
    top: 50,
    right: 50,
    bottom: 50,
    left: 50
  };

  const height = svgHeight - margin.top - margin.bottom;
  const width = svgWidth - margin.left - margin.right;

  // data
  const pizzasEatenByMonth = [15, 5, 25, 18, 12, 22, 0, 4, 15, 10, 21, 2];
  const months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ];

  // append svg and group
  const svg = d3.select(".chart")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);

  const chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

  // scales
  const xScale = d3.scaleLinear()
    .domain([0, pizzasEatenByMonth.length])
    .range([0, width]);

  const yScale = d3.scaleLinear()
    .domain([0, d3.max(pizzasEatenByMonth)])
    .range([height, 0]);

  // line generator
  const line = d3.line()
    .x((d, i) => xScale(i))
    .y(d => yScale(d));

  // create path
  chartGroup.append("path")
    .attr("d", line(pizzasEatenByMonth))
    .attr("fill", "none")
    .attr("stroke", "blue");

  // append circles to data points
  const circlesGroup = chartGroup.selectAll("circle")
    .data(pizzasEatenByMonth)
    .enter()
    .append("circle")
    .attr("cx", (d, i) => xScale(i))
    .attr("cy", d => yScale(d))
    .attr("r", "5")
    .attr("fill", "red");

  // Step 1: Append a div to the body to create tooltips, assign it a class
  // =======================================================
  const toolTip = d3.select("body").append("div")
    .attr("class", "tooltip");

  // Step 2: Add an onmouseover event to display a tooltip
  // ========================================================
  circlesGroup.on("mouseover", function(d, i) {
    toolTip.style("display", "block");
    toolTip.html(`Pizzas eaten: <strong>${pizzasEatenByMonth[i]}</strong>`)
      .style("left", d3.event.pageX + "px")
      .style("top", d3.event.pageY + "px");
  })
    // Step 3: Add an onmouseout event to make the tooltip invisible
    .on("mouseout", function() {
      toolTip.style("display", "none");
    });
}

// When the browser loads, makeResponsive() is called.
makeResponsive();

// When the browser window is resized, responsify() is called.
d3.select(window).on("resize", makeResponsive);
