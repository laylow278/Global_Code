import pyowm

owm = pyowm.OWM('{API-KEY}')
observation = owm.weather_hour_forcast('Kumasi, GH')
w = observation.get_weather()

w.get_wind()
w.get_humidity()
