// Create an initial map object
// Set the longitude, latitude, and the starting zoom level
const myMap = L.map("map").setView([45.52, -122.67], 13);

// Add a tile layer (the background map image) to our map
// Use the addTo method to add objects to our map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

// Create a new marker
L.marker([45.52, -122.67]).addTo(myMap);

// Create a circle and pass in some initial options


// Create a Polygon and pass in some initial options


// Coordinates for each point to be used in the polyline
let line = [
  [45.51, -122.68],
  [45.50, -122.60],
  [45.48, -122.70],
  [45.54, -122.75]
];

// Create a polyline using the line coordinates and pass in some initial options


// Create a rectangle and pass in some initial options

