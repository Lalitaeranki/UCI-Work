// Create a map object
const myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
  accessToken: API_KEY
}).addTo(myMap);

// Define a markerSize function that will give each city a different radius based on its population


// Each city object contains the city's name, location and population
let cities = [
  {
    name: "New York",
    location: [40.7128, -74.0059],
    population: 8550405
  },
  {
    name: "Chicago",
    location: [41.8781, -87.6298],
    population: 2720546
  },
  {
    name: "Houston",
    location: [29.7604, -95.3698],
    population: 2296224
  },
  {
    name: "Los Angeles",
    location: [34.0522, -118.2437],
    population: 3971883
  },
  {
    name: "Omaha",
    location: [41.2524, -95.9980],
    population: 446599
  }
];

// Loop through the cities array and create one marker for each city object
for (var i = 0, ii = cities.length; i < ii; i++) {
  
}
