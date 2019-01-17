// data
const dataArray = [1, 2, 3];
const dataCategories = ["one", "two", "three"];

// svg container
const svgHeight = 400;
const svgWidth = 1000;

// margins
const margin = { top: 50, right: 50, bottom: 50, left: 50 };

// chart area minus margins
const chartHeight = svgHeight - margin.top - margin.bottom;
const chartWidth = svgWidth - margin.left - margin.right;

// create svg container
const svg = d3.select("#svg-area").append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);

// shift everything over by the margins
const chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// scale y to chart height


// scale x to chart width


// create axes


// set the x axis to the bottom of the chart


// set the y axis


// Append Data to chartGroup
