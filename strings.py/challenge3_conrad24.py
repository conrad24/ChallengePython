print("Welcome to the Temperature Conversion App ")
grades = float(input("What is the given Temperature in degrees Fahreinheit: "))
print(f'Degrees Fahrenheit: {grades}')
print(f'Degrees Celsius: {round((grades-32) * 5/9,4)}')
print(f'Degrees Kelvin: {round((grades-32) * 5 / 9 + 273.15,4)}')