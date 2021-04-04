"""
print(type('7'))
print(type(7))
print(type(7.1))

print(isinstance('7',str))
print(isinstance(7,int))
print(isinstance(7.1,float))


print(isinstance(7,str))
print(isinstance('7',int))
print(isinstance('7.1',float))


print(type('7') == str)
print(type(7) == int)
print(type(7.1) == float)

print(type(7) == str)
print(type('7') == int)
print(type('7.1') == float)

numeric_value = '7'
print(numeric_value.isnumeric())

string_value = 'Bob'
print(string_value.isnumeric())

first_value = input('First Number: ')
second_value = input('Second Number: ')

if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print('Please enter number only.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))

first_value = 5
second_value = 4

sum = first_value + second_value
difference = first_value - second_value
product = first_value * second_value
quotient = first_value / second_value
modulus = first_value % second_value
exponent = first_value ** second_value 

print('Sum: ' + str(sum))
print('Difference: ' + str(difference))
print('Product: ' + str(product))
print('Quotient: ' + str(quotient))
print('Modulus: ' + str(modulus))
print('Exponent: ' + str(exponent))



fh = input('What is the temperature in fahrenheit? ')
 
if fh.isnumeric() == False:
    print('Input is not number.')
    exit()

celsius = (float(fh) - 32) * 5/9

print('Temperature in celsius is ', int(celsius) )
"""
print("Simple calculator!")

print("First number")
number = input()







































