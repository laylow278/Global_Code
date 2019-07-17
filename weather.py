import pyowm

owm = pyowm.OWM('103203a3c4ec1f2b9ddca89b33a3e5b')
observation = owm.weather_hour_forcast('Kumasi, GH')
w = observation.get_weather()

w.get_wind()
w.get_humidity()
