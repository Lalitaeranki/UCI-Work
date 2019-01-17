// Step 1: Set up our chart
//= ================================
const svgWidth = 960;
const svgHeight = 500;

const margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 50
};

const width = svgWidth - margin.left - margin.right;
const height = svgHeight - margin.top - margin.bottom;

// Step 2: Create an SVG wrapper,
// append an SVG group that will hold our chart,
// and shift the latter by left and top margins.
// =================================
const svg = d3
  .select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

const chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Step 3:
// Import data from the donuts.csv file
// =================================
d3.csv("donuts.csv", function(error, donutData) {
  if (error) throw error;

  // Step 4: Parse the data
  // Format the data and convert to numerical and date values
  // =================================
  // Create a function to parse date and time
  const parseTime = d3.timeParse("%d-%b");

  // Format the data
  donutData.forEach(function(data) {
    data.date = parseTime(data.date);
    data.morning = +data.morning;
    data.evening = +data.evening;
  });

  // Step 5: Create Scales
  //= ============================================
  const xTimeScale = d3.scaleTime()
    .domain(d3.extent(donutData, d => d.date))
    .range([0, width]);

  const yLinearScale1 = d3.scaleLinear()
    .domain([0, d3.max(donutData, d => d.morning)])
    .range([height, 0]);

  const yLinearScale2 = d3.scaleLinear()
    .domain([0, d3.max(donutData, d => d.evening)])
    .range([height, 0]);

  // Step 6: Create Axes
  // =============================================
  const bottomAxis = d3.axisBottom(xTimeScale).tickFormat(d3.timeFormat("%d-%b"));
  const leftAxis = d3.axisLeft(yLinearScale1);
  const rightAxis = d3.axisRight(yLinearScale2);


  // Step 7: Append the axes to the chartGroup - ADD STYLING
  // ==============================================
  // Add bottomAxis
  chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  // CHANGE THE TEXT TO THE CORRECT COLOR
  chartGroup.append("g")
    .attr("stroke", "green") // NEW!
    .call(leftAxis);

  // CHANGE THE TEXT TO THE CORRECT COLOR
  chartGroup.append("g")
    .attr("transform", `translate(${width}, 0)`)
    .attr("stroke", "orange") // NEW!
    .call(rightAxis);


  // Step 8: Set up two line generators and append two SVG paths
  // ==============================================
  // Line generators for each line
  const line1 = d3
    .line()
    .x(d => xTimeScale(d.date))
    .y(d => yLinearScale1(d.morning));

  const line2 = d3
    .line()
    .x(d => xTimeScale(d.date))
    .y(d => yLinearScale2(d.evening));

  // Append a path for line1
  chartGroup.append("path")
    .data([donutData])
    .attr("d", line1)
    .classed("line green", true);

  // Append a path for line2
  chartGroup.append("path")
    .data([donutData])
    .attr("d", line2)
    .classed("line orange", true);

  // NEW! Step 9: Add color coded titles to the x-axis
  // YOUR CODE HERE

  chartGroup.append("text")
    // Position the text
    // Center the text:
    // (https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/text-anchor)
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 20})`)
    .attr("text-anchor", "middle")
    .attr("font-size", "16px")
    .attr("fill", "green")
    .text("Morning Donut Craving Level");

  chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 37})`)
    .attr("text-anchor", "middle")
    .attr("font-size", "16px")
    .attr("fill", "orange")
    .text("Evening Donut Craving Level");

});
