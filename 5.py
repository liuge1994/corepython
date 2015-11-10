# name = 'Gumby'
# salutation = 'Mr.'
# greeting = 'Hello'
# print(greeting, salutation, name)

# d = {'x': 1, 'y': 2, 'z': 3}
# for key in d:
# 	print(key, 'corresponds to', d[key])

# for key, value in d.items():
# 	print(key, 'corresponds to', value)

# names = ['name', 'beth', 'george', 'damon']
# ages = [12, 45, 32, 102]
# for i in range(len(names)):
# 	print(names[i], 'is', ages[i], 'years old')

# print(list(zip(names, ages)))
# for name, age in zip(names, ages):
# 	print(name, 'is', age, 'years old')

# print(list(zip(range(5), range(10000000))))

# for string in strings:
# 	if 'xxx' in string:
# 		index = strings.index(string)
# 		strings[index] = '[censored]'

# index = 0
# for string in strings:
# 	if 'xxx' in string:
# 		strings[index] = '[censored]'
# 	index += 1

# for index, string in enumerate(strings):
# 	if 'xxx' in string:
# 		strings[index] = '[censored]'

# from math import sqrt
# for n in range(99, 0, -1):
# 	root = sqrt(n)
# 	if root == int(root):
# 		print(n)
# 		break

# for x in seq:
# 	if condition1: continue
# 	if condition2: continue
# 	if condition3: continue

# 	do_something()
# 	do_something_else()
# 	do_another_thing()
# 	etc()

# for x in seq:
# 	if not (condition1 or condition2 or condition3):
# 		do_something()
# 		do_something_else()
# 		do_another_thing()
# 		etc()

# word = 'dummy'
# while word:
# 	word = input('Please enter a word: ')
# 	print('The word was ' + word)

# word = input('Please enter a word: ')
# while word:
# 	print('The word was ' + word)
# 	word = input('Please enter a word: ')

# while True:
# 	word = input('Please enter a word: ')
# 	if not word: break
# 	print('The word was ' + word)
#
# list comprehension
# print([x*x for x in range(10)])
# print([x*x for x in range(10) if x % 3 == 0])
# print([(x, y) for x in range(3) for y in range(3)])

# result = []
# for x in range(3):
# 	for y in range(3):
# 		result.append((x, y))

# print(result)

# girls = ['alice', 'bernice', 'clarice']
# boys = ['chris', 'arnold', 'bob']
# print([b+'+'+g for b in boys for g in girls if b[0] == g[0]])

# letterGirls = {}
# for girl in girls:
# 	letterGirls.setdefault(girl[0], []).append(girl)
# print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

