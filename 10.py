# import sys                                         
# args = sys.argv[1:]                                  
# args.reverse()                       
# print(' '.join(args))                 
                                           
# import fileinput                          
                                            
# for line in fileinput.input(inplace=True):             
# 	line = line.rstrip()                                   
# 	num = fileinput.lineno()                                
# 	print('%-60s # %2i' % (line, num))       

# print(set(range(10))) 
# print(set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])) 
# print(['foe', 'fee', 'fie'])             

# a = set([1, 2, 3]) 
# b = set([2, 3, 4])
# print(a.union(b))
# print(a | b)

# c = a & b
# print(c.issubset(a))
# print(c <= a)
# print(c.issuperset(a))
# print(c >= a)
# print(a.intersection(b))
# print(a & b)
# print(a - b)
# print(a.symmetric_difference(b))
# print(a ^ b)
# print(a.copy())
# print(a.copy() is a)


# mySets = []
# for i  in range(10):
# 	mySets.append(set(range(i, i+5)))
# reduce(set.union, mySets)

# from heapq import *
# from random import shuffle
# data = range(10)
# shuffle(data)
# heap = []
# for n in data:
# 	heappush(heap, n)
# print(heap)

# from random import *
# from time import *
# date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
# time1 = mktime(date1)
# date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
# time2 = mktime(date2)
# random_time = uniform(time1, time2)
# print(asctime(localtime(random_time)))

# import fileinput, random
# fortunes = list(fileinput, input())
# print(random.choice(fortunes))

# from random import shuffle
# from pprint import pprint
# values = list(range(1, 11)) + 'Jack Queen King'.split()
# suits = 'diamonds clubs hearts spades'.split()
# deck = ['%s of %s' % (v, s) for v in values for s in suits]

# shuffle(deck)
# pprint(deck[:])
# while deck: input(deck.pop())
# print(range(1, 10))

# import shelve
# s = shelve.open('test.dat')
# s['x'] = ['a', 'b', 'c']
# s['x'].append('d')
# # print(s['x'])

# temp = s['x']
# temp.append('d')
# s['x'] = temp
# print(s['x'])

# import sys, shelve

# def store_person(db):
# 	"""
# 	Query user for data and stroe it in the shelf object
# 	"""

# 	pid = int(input('Enter unique ID number: '))
# 	person = {}
# 	person['name'] = input('Enter name: ')
# 	person['age'] = input('Enter age: ')
# 	person['phone'] = input('Enter phone number: ')

# 	db[pid] = person

# def lookup_person(db):
# 	"""
# 	Query user for ID and desired field. and fetch the corresponding data from
# 	the shelf object
# 	"""

# 	pid = int(input('Enter ID number: '))
# 	field = input('What would you like to know? (name, age, phone) ')
# 	field = field.strip().lower()
# 	print(field.capitalize() +  ':', \
# 		db[pid][field])

# def print_help():
# 	print('The available commands are: ')
# 	print('store : Stores information about a person')
# 	print('looup : Looks up a person from ID number')
# 	print('quit  : Save changes and exit')
# 	print('?     : Print this message')

# def enter_command():
# 	cmd = input('Enter command (? for help):')
# 	cmd = cmd.strip().lower()
# 	return cmd

# def main():
# 	database = shelve.open('C://database.dat') # You may want to change this name
# 	try:
# 		while True:
# 			cmd = enter_command()
# 			if cmd == 'store':
# 				store_person(database)
# 			elif cmd == 'lookup':
# 				lookup_person(database)
# 			elif cmd == '?':
# 				print_help()
# 			elif cmd == 'quit':
# 				return
# 	finally:
# 		database.close()

# if __name__ == '__main__': main()

import re

# some_text = 'alpha, beta,,,,gamma delta'
# a = re.split('[, ]+', some_text)
# print(a)
# print(re.split('[, ]+', some_text, maxsplit=2))
# print(re.split('[, ]+', some_text, maxsplit=1))

# pat = '[a-zA-Z]+'
# text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
# print(re.findall(pat, text))

# pat = r'[.?\-",]+'
# print(re.findall(pat, text))

# pat = '{name}'
# text = 'Dear {name}...'
# print(re.sub(pat, 'Mr. Gumby', text))

# print(re.escape('www.python.org'))
# print(re.escape('But where is the ambiguity?'))

# m = re.match(r'www\.(.*)\..{3}', 'www.python.org')
# print(m.group(1))
# print(m.start(1))
# print(m.end(1))
# print(m.span(1))

emphasis_pattern = r'\*([^\*]+)\*'

print(re.sub(emphasis_pattern, r'<em>\1</em>', 'Hello, *world*!'))