const cityinput = document.getElementById("city-input");
const searchbtn = document.getElementById("search-btn");
const weatherIcon = document.getElementById("weather-icon");
cityinput.addEventListener("keypress", function(event){
    if(event.key === "Enter"){
        searchbtn.click();
    }
});
searchbtn.addEventListener("click", function (e) {
  const city = cityinput.value;
  if(city.trim() === ""){
    alert("Please enter a city.");
    document.getElementById("text-content").style.display = "none";
    return;
}
  getWeather(city);
});
async function getWeather(city){
  try{
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=602a142539304ffe60bd48026338c37c&units=metric`);
    const data = await response.json();
    if(data.cod == "404"){
      document.getElementById("error").style.display="block";
      document.getElementById("text-content").style.display="none";
      return;
    }
    else{
      document.getElementById("cityName").innerHTML = `City: ${data.name}`;
      document.getElementById("temp").innerHTML =Math.floor(data.main.temp) + "°C";
      document.getElementById("description").innerHTML =data.weather[0].description;
      document.getElementById("humidity-value").innerHTML =data.main.humidity + "%";
      document.getElementById("wind-value").innerHTML =data.wind.speed + " km/h";
      let icon = data.weather[0].main;
      console.log(icon);
      if (icon == "Rain") {
        weatherIcon.src = "rain.png";
      } 
      else if (icon == "Clouds") {
        weatherIcon.src = "clouds.png";
      } 
      else if (icon == "Clear") {
        weatherIcon.src = "clear.png";
      } 
      else if (icon == "Drizzle") {
        weatherIcon.src = "drizzle.png";
      } 
      else if (icon == "Mist") {
        weatherIcon.src = "mist.png";
      } 
      else if (icon == "Snow") {
        weatherIcon.src = "snow.png";
      }
      document.getElementById("text-content").style.display = "block";
      document.getElementById("error").style.display = "none";
    }
  }
  catch (error) {
  console.error("Error fetching weather data:", error);
  document.getElementById("error").style.display = "block";
  document.getElementById("text-content").style.display = "none";
  }
}


