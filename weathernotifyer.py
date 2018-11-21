import pyowm
import datetime
import time
from win10toast import ToastNotifier



def get_weather_data():
    toaster = ToastNotifier()
    owm = pyowm.OWM("6a64010047bb47bcde87e6191871fc02")
    obs = owm.weather_at_place("Exeter,uk")
    w = obs.get_weather()
    wind = w.get_wind()
    humidity = w.get_humidity()
    rain = w.get_rain()
    temp = w.get_temperature("celsius")
    tomorrow = pyowm.timeutils.tomorrow()
    temperature_now = temp["temp"]
    wind_now = wind["speed"]

    weather_data = "the temperature now is: "+ str(temperature_now) + " °C" + " the wind speed is: " + str(wind_now) +" MPH" + " the current humidity is " + str(humidity) + "%" + " the current rain fall is" + str(rain) + "%"
    print(weather_data)
    toaster.show_toast("weather data now in your location",weather_data,icon_path=None,duration=10,threaded=True)
    while toaster.notification_active():
        time.sleep(0.1)

while True:
        excute_time = datetime.datetime.now()
        time.sleep(10)
        get_weather_data()
        print("last executed at" + str(excute_time))



