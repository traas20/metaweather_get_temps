#imports requests for the api call, concurrent.futures for threading, and the mean function from numpy
import requests
import concurrent.futures
from numpy import mean

#define function to pull weather data given a location id
#pulls api response from metaweather.com 
#creates temps array and appends the max_temp for each day that was given under consolidated_weather
#prints the name of the location and the average max temperature for the six day forecast
def get_avg_temp(location):
    weather = requests.get('https://www.metaweather.com/api/location/' + location +'/')
    temps = []
    for temp in range(len(weather.json()['consolidated_weather'])):
        temps.append(weather.json()['consolidated_weather'][temp]['max_temp'])
    print(weather.json()['title'] + ' Average Max Temp: ' + str(round(mean(temps),2)))


#stores the location ids for SLC, Boise, and LA in locations array
locations = ['2487610', '2442047', '2366355']

#runs the get_av_temp function using threading
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(get_avg_temp, locations)