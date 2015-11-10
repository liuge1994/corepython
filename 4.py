#!/usr/bin/env python

# index
# names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl'] 
# numbers = ['1024', '9102', '0910', '0112']
# print(numbers[names.index('Cecil')])

# x = {}
# x[42] = 'Foobar'
# print(x)

# people = {
# 	'Alice': {
#       'phone': '2341',
#       'addr': 'Foo drive 23'
# 	},
# 	'Beth': {
# 	    'phone': '9102',
# 	    'addr': 'Bar street 42'
# 	},
# 	'Cecil': {
# 	    'phone': '3158',
# 	    'addr': 'Baz avenue 90'
# 	}
# }

# labels = {
# 	'phone': 'phone number',
# 	'addr': 'address'
# }

# name = input('Name: ')

# # sorting the number of phone or the address
# request = input('Phone number (p) or address (a)?')

# # use the true key
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'

# if name in people: print("%s's %s is %s." % \
#     (name, labels[key], people[name][key]))

# clear
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)
returned_value = d.clear()
print(d)
print(returned_value)