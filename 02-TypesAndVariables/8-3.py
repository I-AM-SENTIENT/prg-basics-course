# A program that reads the radius of a circle from the keyboard.

temperatureC = float(input('Enter the temperature in Celsius: '))
temperatureF = round(temperatureC * 9/5 + 32, 2)
temperatureK = round(temperatureC + 273.15, 2)
print(f'The temperature in Kelvin is {temperatureK}.')
print(f'The temperature in Fahrenheit is {temperatureF}.')