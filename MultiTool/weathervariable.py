from pyowm import OWM
import povtvariable
import time
from pyowm.commons.exceptions import NotFoundError
import placevariable

while povtvariable.povt==True:
	try:

		owm = OWM("e3bcef960f4cc6c7b370b0b90c4e211f")
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place(placevariable.place)
		w = observation.weather
		ds = w.detailed_status
		t = w.temperature("celsius")["temp"]	

		povtvariable.povt=False
	except NotFoundError:
		print("Oh no! I don't know this place! Where is it, on mars?")
