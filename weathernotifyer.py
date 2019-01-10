import pyowm
import datetime
import time as timer
from win10toast import ToastNotifier
import os.path


def get_weather_data(loc, unit):
    """

    :param loc: physical location
    :param unit: F/C
    :return:
    """
    toaster = ToastNotifier()
    owm = pyowm.OWM("6a64010047bb47bcde87e6191871fc02")
    obs = owm.weather_at_place(loc)
    w = obs.get_weather()
    wind = w.get_wind()
    humidity = w.get_humidity()
    rain = w.get_rain()
    temp = w.get_temperature(unit)
    tomorrow = pyowm.timeutils.tomorrow()
    temperature_now = temp["temp"]
    wind_now = wind["speed"]

    if len(rain) == 0:
        rain = "no rain in your area now"

    time = datetime.datetime.now()
    weather_data = "the temperature now is: " + str(temperature_now) + " °C" + " the wind speed is: " + str(
        wind_now) + " MPH" + " the current humidity is " + str(humidity) + "%" + " the current rain fall is" + str(
        rain) + "%" + str(time)
    print(weather_data)
    toaster.show_toast("weather data now in your location", weather_data, icon_path=None, duration=10, threaded=True)
    while toaster.notification_active():
        timer.sleep(0.1)

def main():
    """
    Get user variables, run script
    :return:
    """
    # Location for settings
    settings = "settings/config.ini"
    # Check if file exists, if not make it
    if not os.path.isfile(settings):
        import setUpUserData as setUp
        setUp.makeFile()
    # Get the User variables
    with open(settings, "r") as config:
        userData = config.read()
        userData = userData.split("#")
        location, tempUnit, notificationInterval = userData

    # run the toasts
    while True:
        excute_time = datetime.datetime.now()
        timer.sleep(int(notificationInterval))
        get_weather_data(location, tempUnit)
        print("last executed at" + str(excute_time))

if __name__ == '__main__':
    main()