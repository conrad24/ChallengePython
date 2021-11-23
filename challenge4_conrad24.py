import math

print('Welcome to the Right Triangle Solver App ')
first_leg = float(input('what is the first leg of the triangle: '))
second_leg = float(input('What is the second leg of the triangle: '))
hipotenusa = math.sqrt((first_leg**2) + (second_leg**2))
print(f'For a triangle with legs of {first_leg} and {second_leg} the hypotenuse is {round(hipotenusa,3)}')
area = first_leg * second_leg / 2
print(f'For a triangle with legs of {first_leg} and {second_leg} the area is {round(area,3)}')