#defining the function
def temperature(celcius):
    fehrenheit = ((9*celcius)/5) + 32
    print(f"{celcius} celcius is equal to : {round(fehrenheit,2)} fehrenheit")
    
celcius = float(input("How many degree celcius you want to convert into degree fehrenheit : "))

#calling the function by passing one argument
temperature(celcius)
