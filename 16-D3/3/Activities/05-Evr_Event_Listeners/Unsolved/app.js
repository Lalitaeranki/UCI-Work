// data
const dataArray = [1, 2, 3];
const dataCategories = ["one", "two", "three"];

function makeResponsive() {

    // if the SVG area isn't empty when the browser loads, remove it and replace it with a resized version of the chart
  const svgArea = d3.select("body").select("svg");

  if (!svgArea.empty()) {
    svgArea.remove();
  }

    // svg container
  const svgHeight = window.innerHeight;
  const svgWidth = window.innerWidth;

    // margins
  const margin = {
    top: 50,
    right: 50,
    bottom: 50,
    left: 50
  };

    // chart area minus margins
  const chartHeight = svgHeight - margin.top - margin.bottom;
  const chartWidth = svgWidth - margin.left - margin.right;

    // create svg container
  const svg = d3.select("body").append("svg")
        .attr("height", svgHeight)
        .attr("width", svgWidth);

    // shift everything over by the margins
  const chartGroup = svg.append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);

    // scale y to chart height
  const yScale = d3.scaleLinear()
        .domain([0, d3.max(dataArray)])
        .range([chartHeight, 0]);

    // scale x to chart width
  const xScale = d3.scaleBand()
        .domain(dataCategories)
        .range([0, chartWidth])
        .padding(0.1);

    // create axes
  const yAxis = d3.axisLeft(yScale);
  const xAxis = d3.axisBottom(xScale);

    // set x to the bottom of the chart
  chartGroup.append("g")
        .attr("transform", `translate(0, ${chartHeight})`)
        .call(xAxis);

    // set y to the y axis
  chartGroup.append("g")
        .call(yAxis);

  chartGroup.selectAll("rect")
        .data(dataArray)
        .enter()
        .append("rect")
        .attr("x", (d, i) => xScale(dataCategories[i]))
        .attr("y", d => yScale(d))
        .attr("width", xScale.bandwidth())
        .attr("height", d => chartHeight - yScale(d))
        .attr("fill", "green");
        // event listener for onclick event

        // event listener for mouseover

        // event listener for mouseout

}

makeResponsive();

// Event listener for window resize.
// When the browser window is resized, makeResponsive() is called.
d3.select(window).on("resize", makeResponsive);
