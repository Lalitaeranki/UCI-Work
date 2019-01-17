d3.selectAll("select").on("change", function() {
  if(this.id){
    if(this.id == "shapes"){
      shapeFilter(this.value);
    } else if (this.id == "city"){
      cityFilter(this.value);
    }
  }
});

d3.selectAll("li").on("click", function() {
  // you can select the element just like any other selection
  var listItem = d3.select(this);
  listItem.style("color", "blue");

  var listItemText = listItem.text();
  console.log(listItemText);
});
