from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError#s, ConnectionError
from colorama import init
from colorama import Fore, Back, Style
import povtvariable
import weathervariable
import placevariable

init()

povtvariable.povt=True

while povtvariable.povt==True:
    try:
        print("Temperature in city (or village) " + placevariable.place + " is " + str(weathervariable.t) + \
                                                     "C. " + "Status is " + weathervariable.ds)
        import wearsubmodule

    except NotFoundError:
        print("Oh no! I don't know this place! Where is it, on mars?")

    #except ConnectionError:
        #print("Oh no! Where is internet-connection?")

    povto = input("Retry? (y, n): ")

    if povto == "y":
        povtvariable.povt=True
    elif povto == "n":
        povtvariable.povt=False
        raise SystemExit
    else:
        povtvariable.povt=False
        print("Hm, okay... Maybe " + povto + " is no")
        raise SystemExit
        
