// SVG wrapper dimensions are determined by the current width
// and height of the browser window.
const svgWidth = 1200;
const svgHeight = 660;

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
  .attr("stroke", "green");

// append circles to data points, add transitions
// Hint:  You may have to alter this code for the transition on page load
const circlesGroup = chartGroup.selectAll("circle")
  .data(pizzasEatenByMonth)
  .enter()
  .append("circle")
  .attr("cx", (d, i) => xScale(i))
  .attr("cy", d => yScale(d))
  .attr("r", "10")
  .attr("fill", "red");

// YOUR CODE HERE


