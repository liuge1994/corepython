#!/usr/bin/python
# from math import pi

# print('%10f' % pi)
# print('%10.2f' % pi)
# print('%.2f' % pi)
# print('%.5s' % 'Guido van Rossum')
# print('%.*s' % (5, 'Guido van Rossum'))

# print('%010.2f' % pi)

# print(0o10)

# print('%-10.2f1' % pi)
# print(('% 5d' % 10) + '\n' + ('% 5d' % -10))
# print(('%+5d' % 10) + '\n' + ('%+5d' % -10))

# print('With a moo-moo here, and a moo-moo there'.find('moo'))
# title = "Monty Python's Flying Circus"
# print(title.find('Monty'))
# print(title.find('Python'))
# print(title.find('Flying'))
# print(title.find('Zirquss'))
# subject = '$$$ Get rich now!!! $$$'
# print(subject.find('$$$'))
# print(subject.find('$$$', 1))
# print(subject.find('!!!'))
# print(subject.find('!!!', 0, 16))

# join
# seq = ['1', '2', '3', '4', '5']
# sep = '+'
# print(sep.join(seq))
# dirs = '', 'user', 'bin', 'env'
# print('/'.join(dirs))
# print('C:' + '\\'.join(dirs))

# lower
# print('Trondheim Hammer Dance'.lower())
# if 'Gumby' in ['gumby', 'smith', 'jones']: print('Fount it')
# name = 'Gumby'
# names = ['gumby', 'smith', 'jones']
# if name.lower() in names: print('Found it!')

# replace
# print('This is a test'.replace('is', 'eez'))

# split
# print('1+2+3+4+5'.split('+'))
# print('/usr/bin/env'.split('/'))
# print('Using the default'.split())

# translate
# from string import maketrans

table = str.maketrans('cs', 'kz')
print(len(table))
print(table[97:123])
print(str.maketrans('', '')[97:123])