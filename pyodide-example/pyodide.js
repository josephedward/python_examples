
// openweathermaps
// d3104375bd592736cf8775886538ee2a

async function main() {
    await loadPyodide({ indexURL : "https://cdn.jsdelivr.net/pyodide/v0.17.0/full/" });
    // Pyodide is now ready to use...
//     console.log(pyodide.runPython(`
//       import sys
//       sys.version
//       import matplotlib.pyplot as plt
// import pandas as pd
// import numpy as np
// import requests
// import time
// import seaborn as sea
// # does conversion for us
// units = "imperial"

// weather_api_key = "d3104375bd592736cf8775886538ee2a"

// # define url
// query_url = f"http://api.openweathermap.org/data/2.5/weather?appid={weather_api_key}&units={units}&q="


// city_names = []
// cloudinesses = []
// dates = []
// humidities = []
// lats = []
// lngs = []
// max_temps = []
// wind_speeds = []
// countries = []

// pass_count = 0
// set_count = 1

// city= "richmond"
//     # print(city)

// response = requests.get(query_url + city).json()
// print(response)
//     `));
  };
  main();
  