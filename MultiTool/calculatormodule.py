from colorama import init
init()
from colorama import Fore, Back, Style
import povtvariable

povtvariable.povt = True

print(Fore.GREEN + "\nSuR - calculator with sweet bread flavor")

while povtvariable.povt == True:
        

    what = input(Fore.WHITE + "\nAction? " + Fore.GREEN + "(+,-, x, /): " + Fore.YELLOW)
        
    a = input (Fore.WHITE + "First number: " + Fore.YELLOW)

    b = input(Fore.WHITE + "Second number: " + Fore.YELLOW) 
        
    psh = input("Enter any symbol: ")
    if psh == "=":
        if not a:
            a=0
        if not b:
            b=0
    else:
        if not a:
            a=0
        if not b:
            b=0
        
    if what == "+":
        try:   
            c=float(a)+float(b)
            print(Back.YELLOW + Fore.BLACK + "Addition result:" + str(c))
        except ValueError:
            print(Fore.BLACK + Back.RED +"Please, enter only numbers!")
        
    elif what == "-":
        try:
            c=float(a)-float(b)
            print(Back.YELLOW + Fore.BLACK +"Subtraction result:" + str(c))
        except ValueError:
            print(Fore.BLACK + Back.RED + "Please, enter only numbers!")
        
    elif what == "×":
         try:   
            c=float(a)*float(b)
                
            print(Back.YELLOW + Fore.BLACK +"Multiplication result:" + str(c))
         except ValueError:
           print(Fore.BLACK + Back.RED +"Please, enter only numbers!")
            
    elif what == "/":
        try:
            c=float(a)/float(b)
            print(Back.YELLOW + Fore.BLACK +"Division result:" + str(c))
        except ValueError:
            print(Fore.BLACK + Back.RED +"Please, enter only numbers!!")
        except ZeroDivisionError:
            print("Uh-oh! Zero division!")
    
    else:
        print(Back.RED + Fore.BLACK + "Sorry, i don't know what a " + what + " is, but i'll try to find out what it is  > ͜ 0 ")
            
    povto = input("Retry? (y, n): " + Back.BLACK + Fore.YELLOW)
        
    if povto == "n":
        povtvariable.povt = False
            
    elif povto == "y":
        povtvariable.povt = True
            
    else:
        povtvariable.povt = False
        print(Back.RED + Fore.BLACK + "Hmmmm. Okay. Maybe " + povto + " is no? > ͜ 0")
