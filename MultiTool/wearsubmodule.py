import weathervariable

if ((weathervariable.t >= 18) and (weathervariable.t <= 25)):
    if weathervariable.ds == "rain":
        print("It's warm, but raining. Take your umbrella.")
    else:
        print("It's warm now! Wear shorts and a t-shirt.")

elif ((weathervariable.t >= 26) and (weathervariable.t <= 35)):
    if weathervariable.ds == "rain":
        print("It's very warm, go chill in the rain.")
    else:
        print("Oh jeez! It's so hot in there! Sit under three fans!")
elif weathervariable.t >=36:
    print("OH F... RIED POTATO! DON'T GO OUTSIDE! YOU F... INISH YOUR LIFE IF GO OUTSIDE!")

elif ((weathervariable.t >= 8) and (weathervariable.t <= 17)):
    if weathervariable.ds == "rain":
        print("It's cold and rainy. Take umbrella and wear windbreaker, sweatshirt or sweater and pants.")
    else:
        print("It's little bit cold, wear sweater or sweatshirt and pants")
elif ((weathervariable.t >= 0) and (weathervariable.t <= 7)):
    if weathervariable.ds == "rain":
        print("It's cold, wear spring coat, sweatshirt or sweater, pants, hat and put your umbrella.")
    else:
        print("It's cold, wear spring coat, sweatshirt or sweater, pants and hat.")
elif ((weathervariable.t >= -18) and (weathervariable.t <= -1)):
    if weathervariable.ds == "rain":
        print("It's very cold and rainy, wear winter coat, sweatshirt or sweater, winter pants, hat and put your umbrella.")
    if weathervariable.ds == "snow":
        print("It's very cold and snowy, wear winter coat, sweatshirt or sweater, winter pants and hat.")        
    else:
        print("It's very cold, wear winter coat, sweatshirt or sweater, winter pants and hat.")
elif weathervariable.t <=19:
    print("Oh no, it's very cold! Wear like cabbage!")