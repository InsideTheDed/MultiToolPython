from colorama import init
init()
from colorama import Fore, Back, Style

multitool=True

while multitool==True:

    povtcalc=True
    povtweath=True
    zanov=True

    import povtvariable

    povtvariable.povt=True

    while zanov==True:
        what=input("What can i serve? (calc, weath): ")
        zanov=False

    if what=="calc":
        while povtcalc==True:
            import calculatormodule

            if povtvariable.povt==True:
                povtcalc=True
            elif povtvariable.povt==False:
                povtcalc=False
                zanov=True
    if what=="weath":
        while povtweath==True:
            import weathermodule
    polnzanov=input("Retry Multitool? (y, n): ")
    if polnzanov=="n":
        raise SystemExit
    elif polnzanov=="y":
        multitool=True
    else:
        print("Hmmmm. Okay. Maybe " + polnzanov + " is no? > ͜ 0")
        raise SystemExit
            
        
        
        
