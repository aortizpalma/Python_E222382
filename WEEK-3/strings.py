# What is string?
# A string is a text data type
# You can use '' or ""

letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
print(letters)
print(len(letters))
print(len(vowels))
print(len(consonants))
print(letters.upper())
print(vowels.upper())
print(consonants.upper())
print(dir(letters))

challenge = '30 Days of Python'
print(challenge.upper())
print(challenge.title())
print(challenge.swapcase())
print(challenge.find('0')) # returns the index of the string searched
print(challenge.find('y'))
print(challenge.find('f'))

language = 'Python for human beings'
print(language.upper())
print(len(language))
print(language[0:2])
print(language[2:])
print(language[-1])
print(language[-2:])
print(language[::-1])
print(language.lower())
print(language.title())
print(language.swapcase())
print(language.isupper())
print(language.islower())
print(language.count('o'))

city = '    Mississippi    '
print(city.count('i'))
print(city.count('s'))
print(city.count('p'))
print(city.find('i'))
print(city.rfind('i')) #right find locates the index of the first searched character starting from the right
print(city)
print(city.strip()) # strip removes the spaces
print(city.lstrip()) # strip removes the spaces
print(city.rstrip()) # strip removes the spaces
print(list(city))
print('The index of M is', city.index('M'))
print('The index of i is', city.find('i'))
print('The index of I is', city.find('I')) # find throws a -1 if the string is not found instead of an error. The index method throws an error instead.

print('i love Python'.capitalize())
print('i love Python'.title())

country = 'Finland'
print(country.startswith('Fin'))
print(country.startswith('f'))
print(country.endswith('d'))
print(country.endswith('D'))
print(country.endswith('land'))

skills = ['HTML', 'CSS', 'JS', 'Python']
print(skills)
print(''.join(skills))
print(' '.join(skills))
print(', '.join(skills))

print('abcd'.isalpha()) # Checks if it is in alphabetic order
print('12abcd314'.isalpha()) # Checks if it is in alphabetic order
print('12abcd314'.isalnum()) # Checks if it is alphanumeric
print('123'.isdecimal())
print('123'.isnumeric())
print('123'.isdigit())

# isidentifier helps to check if a variable's name is OK or not
print('year'.isidentifier())
print('2022year'.isidentifier())
print('_year'.isidentifier())
print('$year'.isidentifier())

sentence = 'I love JavaScript. JavaScript is the most important language in this world.' 

print(sentence.replace('JavaScript','Python'))

first_name = 'Al'
last_name = 'Ortiz'
age = 40
country = 'Finland'
city = 'Helsinki'
skills = ['HTML', 'CSS', 'JS', 'Python']
formated_skills = ', '.join(skills)

full_name = first_name + ' ' + last_name
print(full_name)

# Sample string concatenation 1
print('I am ' + full_name + '. I am ' + str(age) + ' years old. I live in ' + city + ', ' + country + '. I have skills in ' + ', '.join(skills) + '.')

# Sample string concatenation 2
print(f'I am {full_name}. I am {age} years old. I live in {city}, {country}. I have skills in {formated_skills}.')


# Sample string concatenation 3
print('I am {}. I am {} years old. I live in {}, {}. I have skills in {}.'.format(full_name, age, city, country, formated_skills))


a = 4
b = 3
print('a + b = ', a + b)
print('%d + %d = %d' %(a, b, a + b)) # %d is used for integers
print('%d / %d = %.3f' %(a, b, a / b)) # %f is used for floating numbers. The number before indicate the number of decimals (e.g. 3)

# The old way of formatting
print('%d - %d = %d' %(a, b, a - b))
print('%d * %d = %d' %(a, b, a * b))
print('%d // %d = %d' %(a, b, a // b))
print('{} % {} = {}'.format(a, b, a % b))
print('%d ** %d = %d' %(a, b, a ** b))


print('%s%s' %('water', 'melon')) # %s is used for strings

# A newer way of formatting
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Another AND recommended way of formatting
div = a/b
print(f'{a} - {b}= {a - b}')
print(f'{a} * {b}= {a * b}')
print(f'{a} / {b}= {div:0.2f}')
print(f'{a} //{b} ={a // b}')
print(f'{a} % {b}= {a % b}')
print(f'{a} **{b} ={a ** b}')


sentence = 'I love Python'
print(sentence)
print(sentence.split())
print(sentence.split(' love '))
print('I love \nPython very well') # \n for a new line
print('Name', '\t', 'Age','\t', 'Country') # \t for a tab
print('John', '\t', '23','\t', 'Finland') # \t for a tab

# \ is used for skipping a character
print('I don\'t like this')
print("I don't like this")
print("The old cliché of \"an apple a day keep the doctor away\" might not work")
print('The old cliché of \"an apple a day keep the doctor away\" might not work')


city = '    Mississippi    '
print(set(city))    # set prints the unique characters of a string and removes the duplicates


