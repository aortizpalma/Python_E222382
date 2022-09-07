# In this file we test built-in functions

'''
- Built-in functions
    - print(), len(), max(), min(), input(), round(), abs(), dir(), str()
'''

print()
print('Hello', 'Something', 2022)
print('I love Python. But I prever JavaScript')
print('I love Python. \nBut I prever JavaScript')

# Length of a string
# String is any data

print('Alfonso')
print("Alfonso")
print("""Alfonso""")

print(len('Alfonso'))
print(len('Finland'))
print(len('Hello World!'))
# print(len(1000000)) throws an error bc len() only works with strings or lists


print(len('555-555-5555'))
print(len('555-555-5555'))

# list data type
nums = [1, 2, 3, 4, 5]
print(len(nums))

names = ['asab', 'John', 'Donald', 'elon']
print('There are', len(names), 'names')

# min, max and sum
print('The minimum value is', min(9,4,-2, 1, 0, -1))
print('The maximum value is', max(9,4,-2, 1, 0, -1))

print(sum([9,4,-2, 1, 0, -1])) # these numbers are only sum if they are part of a list, as otherwise sum would only take two values.

print(round(9.81)) # throws 10
print(round(3.14)) # throws 3
print(round(7.5)) # throws 8
print(round(9.81567, 2)) # throws 9.82


# abs
print(abs(-5))
print(abs(7))
# print(dir(names))
# print(dir('text'))
# print(dir(1))

print(type(1))
print(type(10))
print(type(0))
print(type(2.77))
print(type(1 + 1j))


# string data type
print(type('Alfonso'))
print(type('Finland'))
print(type('Helsinki'))


# print(help('string'))
# print(dir('string'))
# print(dir({}))

countries = ['Finland', 'Sweden', 'Estonia', 'Denmark', 'Norway', 'Finland']
print(dir(countries))
countries.append('Iceland')
countries.append('Russia')
print(countries)
print(countries.count('Finland'))
countries.extend(['Germany', 'Belgium', 'France', 'The Netherlands'])
print(countries)
print(countries.index('Finland'))


print('1' + str(2))
print(int(1)+2)

# Boolean
print(type(True))
print(type(False))

# int() and str()
print('1')
print(type('1'))
print(type(int('1')))
# print('1'+ 1)

print(int('1')+1)
print('1'+str(2))


# range(start, stop, stop)
print(list(range(0,11)))
print('===Whole Numbers===')
print(list(range(0,101)))
print('===Natural Numbers or Counting Numbers===')
print(list(range(1,101)))

print('==== Integers ====')
print(list(range(-100, 101)))

print('==== Even numbers ====')
print(list(range(0,101, 2)))

print('==== Odd numbers ====')
print(list(range(1,101, 2)))

print(list('Alfonso'))


# input
# ANYTHING YOU GET FROM THE USER INPUT IS A STRING
# input allows to get data from a user
first_name = input('Enter your name: ')
country = input('Where are you from?')
year = input('When where you born?')
age = 2022 - int(year)

print('Welcome', first_name)
print('It is great that you ar from', country)
print('You are', age, 'years old')


