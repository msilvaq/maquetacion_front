"""
first_string = 'A literal string'
second_string = "A literal string"
print(first_string == second_string)


thrid_string = 'A single quoted literal string with a " double quote'
fourth_string = "A single quoted literal string with a ' double quote"
print(thrid_string)
print(fourth_string)

fifth_string = 'A single quoted literal string with an \' escaped single quote'
sixth_string = "A double quoted literal string with a \" double quote"
seventh_string = 'A literal string with a \n new line character'
eighth_string = 'A literal string with a \t tab character'

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)

ninth_string = r"A literal string with a \n new line character printed raw"

print(ninth_string)

tenth_string = '''A literal string
on more than one line
sometimes known as a verbatim string'''

eleventh_string = Another literal string
     on more than one line
using double quotes

print(tenth_string)
print(eleventh_string)


first = 'Conrad'
second = 'Grant'
third = 'Bob'

print(first,second)
print(first,second,third)
print(first,second,third,sep='-')
print(first,second,third,sep='-', end='.'"\n")


message = str.capitalize('first message')
print(message)

message = 'first message'.capitalize()
print(message)

message = 'thrid message'
print(message.capitalize())


message = 'hello world'
print(message.lower())
print(message.upper())

message = message.title()
print(message)
print(message.swapcase())

location = 'Mississippi'
print(location.count('s'))


print(len('how many letters in this string?'))

message = 'racecar'
print(message.startswith('r'))
print(message.startswith('a'))
print(message.startswith('ra'))

print(message.endswith('r'))
print(message.endswith('a'))
print(message.endswith('ar'))

message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T'))

message = '    middle     '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')



message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)

message = 'howdy'
print(message.rjust(20))
print(message.rjust(20, '*'))
print(message.ljust(20))
print(message.ljust(20, '/'))

medicine = 'Coughussin'
dosage = 5
duration = 4.5

instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)
print(instructions)


name = 'World'
message = f'Hello, {name}.'
print(message)

count = 10
value = 3.14
message = f'Count to {count}.  Multiply by {value}.'
print(message)

width = 5
height = 10

print(f'The perimeter is {(2 * width) + (2 * height)} and the area is {width * height}.')
value = 'hi'

print(f'.{value:<25}.')
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')
"""



first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
#print(f'{first_value:-^25}'.lower())
first_value = first_value.strip()
first_value = first_value.lower()
first_value = first_value.title()
first_value = f'{first_value:^30}'


# Second challenge
second_value = second_value.replace('-','')
second_value = second_value.strip()
second_value = second_value.capitalize()


# Third challenge  'tH IR D-C HALLE NGE'
third_value = third_value.replace(' ','')
third_value = third_value.replace('-',' ')
third_value = third_value.swapcase()
third_value = f'{third_value:>30}'

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fifth challenge - use only a single print() function. Create tabs and new lines using f-strings.
print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')




















































