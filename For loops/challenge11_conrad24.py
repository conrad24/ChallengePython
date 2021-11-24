print('Welcome to the Binary/Hexadecimal Converter App ')
number = int(input('Compute binary and hexadecimal values up to the following decimal number: '))
print('Generating lists.... complete! ')
print('Using slices, we will now show a portion of each list. ')
number2 = int(input('what decimal number would you like to start at: '))
number3 = int(input('what decimal number would you like to stop at: '))

print(f'\nDecimal values from {number2} to {number3}')
for x in range(number2, number3):
    print(x)

print(f'\nBinary values from {number2} to {number3} ')
for n in range(number2, number3):
    print(bin(n))

print(f'\nHexadecimal values from {number2} to {number3}')
for m in range(number3, number3):
    print(hex(m))

unicorn = input(f'\nPress enter to se all numbers from 1 to {number}. ')
print('Decimal----Binary----Hexadecimal ')
for z in range(1, number):
    print(f'{z},{bin(z)},{hex(z)} ')


