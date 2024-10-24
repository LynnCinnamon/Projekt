//promise html from server
function fetchWeatherHTML() {
    return new Promise((resolve, reject) => {
        const weatherHTML = `
            <div class="weather-widget">
                <p class="temp">Temperature: 15°C</p>
                <p class="temp_range">Temperature Range: 14°C - 16°C</p>
                <p class="weather">Weather: scattered clouds</p>
            </div>`;
        resolve(weatherHTML);
    });
  }
  //insert it to id-placerholder
  fetchWeatherHTML()
    .then(weatherHTML => {
      document.getElementById('weather-placeholder').innerHTML = weatherHTML;
    })
    .catch(error => console.error('Fehler beim Abrufen des Wetter-Widgets:', error));
  
  function fetchTrafficHTML() {
    return new Promise((resolve, reject) => {
        const trafficHTML = `
            <div class="traffic-widget">
                <p class="start_time">Abfahrt</p>
                <p class="end_time">Ankunft</p>
                <p class="time_range">benötigte Zeit</p>
            </div>`;
        resolve(trafficHTML);
    });
  }
  fetchTrafficHTML()
    .then(trafficHTML => {
      document.getElementById('traffic-placeholder').innerHTML = trafficHTML;
    })
    .catch(error => console.error('Fehler beim Abrufen des Wetter-Widgets:', error));