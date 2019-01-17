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

  // Step 5: Create the scales for the chart
  // =================================
  const xTimeScale = d3.scaleTime()
    .domain(d3.extent(donutData, d => d.date))
    .range([0, width]);

  const yLinearScale = d3.scaleLinear().range([height, 0]);

  // Step 6: Set up the y-axis domain
  // ==============================================
  // @NEW! determine the max y value
  // find the max of the morning data
  

  // find the max of the evening data
  

  // Use the yMax value to set the yLinearScale domain
  


  // Step 7: Create the axes
  // =================================
  

  // Step 8: Append the axes to the chartGroup
  // ==============================================
  // Add x-axis
  

  // Add y-axis
  

  // Step 9: Set up two line generators and append two SVG paths
  // ==============================================

  // Line generator for morning data
  

  // Line generator for evening data
  

  // Append a path for line1
  

  // Append a path for line2
  

});
