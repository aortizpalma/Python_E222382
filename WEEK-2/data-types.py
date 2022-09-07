'''- Data types
    - Numbers(Int, Float, Complex)
    - Booleans(True/False)
    - Strings
    - List
    - Set
    - Tuples
    - Dictionary    '''

# Numbers
print(type(2))
print(type(3.14))
print(type(1 + 4j))

# Booleans
print(type(True))
print(type(False))
print(type(4 > 5))
print(type(len('cat') == len('dog')))
print('cat' == 'dog')
print(len('cat') == len('dog'))
print(len('dragon') == len('python'))
print('on' in 'dragon')
print('gon' in 'Python')

# Strings
# Any data type under single or double quotes are strings
letter = 'a'
letters = 'abkjslkfjsalkdfjslkdfjklsadj'
vowels = 'aeiou'
first_name = 'Alf'
country = 'Finland'
sentence = 'Finland is a country'
print(type(letter))
print(len(letter))
print(len(letters))

# List data type, list is a mutable data type and it is also ordereed
nums = [1, 2, 3, 4, 5]
print(len(nums))
print(sum(nums))
crazy_list = [1, 2, False, 'Alf', ('COVID', 2019), [
    'Alf', 'Finland'], {'name': 'Alf'}]
print(len(crazy_list))

# Tuple, it is an order data and immutable
# Tuples can't be modiefied

tpl = (1, 2, 3, 4, 5)
print(tpl)
tpl = (1, 2)
print(tpl)
skills = ('HTML', 'CSS', 'JS', 'Python')
hobbies = ['football', 'basketball']


# Set, is a unique data element without order

st = {1, 2, 3, 4, 5, 5, 5, 6}
print(st)
print(len(st))

# Dictionary
# It is a data structure based on key and value pairs

finnish_to_eng = {
    'kirja': 'book',
    'talo': 'house',
    'Kauppa': 'shop',
    'peruna': 'potato'
}
print(finnish_to_eng)
print(len(finnish_to_eng))


# 3 x 4
arr = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [6, 7, 8, 9]
]
print(arr)