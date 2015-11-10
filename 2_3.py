# sentence = input("Sentence: ")

# screen_width = 80
# text_width = len(sentence)
# box_width = text_width + 6
# left_margin = (screen_width - box_width) // 2
# print()
# print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
# print(' ' * left_margin + '| ' + ' ' * text_width    + ' |')
# print(' ' * left_margin + '| ' +       sentence      + ' |')
# print(' ' * left_margin + '| ' + ' ' * text_width    + ' |')
# print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
# print()

# check the PIN and name of user
# database = [
#     ['albert', '1234'],
#     ['dilbert', '4242'],
#     ['smith', '7524'],
#     ['jones', '9843']
# ]
# username = input('User name: ')
# pin = input(' PIN code: ')

# if [username, pin] in database: print('Access granted')

# format string %
# format = 'Hello, %s. %s enough for ya?'
# values = ('world', 'Hot')
# print(format % values)

# format float %f
# format = 'Pi with three decimals: %.3f'
# from math import pi
# print(format % pi)
# print(pi)

# from string import Template
# s = Template('$x, glorious $x!')
# print(s.substitute(x='slurm'))

# s = Template("It's ${x}tastic!")
# print(s.substitute(x='slurm'))

# s = Template("Make $$ selling $x!")
# print(s.substitute(x='slurm'))

# s = Template('A $thing must never $action.')
# d = {}
# d['thing'] = 'gentleman'
# d['action'] = 'show this socks'
# print(s.substitute(d))

# print('Price of eggs: $%d' % 42)
# print('Hexadecimal price of eggs: %x' % 42)
# from math import pi
# print('Pi: %f...' % pi)
# print('Very inexact estimate of pi: %i' % pi)
# print('Using str: %s' % 42)
# print('Using repr: %r' % 42)

width = int(input('Please enter width: '))

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'

print('=' * width)

print(header_format % (item_width, 'Item', price_width, 'price'))

print('-' * width)

print(format % (item_width, 'Apples', price_width, 0.4))
print(format % (item_width, 'Pears', price_width, 0.5))
print(format % (item_width, 'Cantaloupes', price_width, 1.92))
print(format % (item_width, 'Dried Apricots (16 oz.)', price_width, 8))
print(format % (item_width, 'Prunes (4 1bs.)', price_width, 12))