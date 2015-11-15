# fibs = [0, 1]
# for i in range(8):
# 	fibs.append(fibs[-2] + fibs[-1])

# print(fibs)

# num = input('How many Fibonacci numbers do you want? ')
# num = int(num)
# for i in range(num-2):
# 	fibs.append(fibs[-2] + fibs[-1])

# print(fibs)

# import math 
# x = 1
# y = math.sqrt
# # print(hasattr(y, __call__))
# # print(hasattr(x, __call__))
# print(callable(y))
# print(callable(x))

# def square(x):
# 	'Calculates the square of the number x.'
# 	return x*x

# print(square.__doc__)
# print(help(square))

# def try_to_change(n):
# 	n = 'Mr. Gumby'

# name = 'Mrs. Entity'
# try_to_change(name)
# print(name)

# def change(n):
# 	n[0] = 'Mr. Gumby'

# names = ['Mr. Entity', 'Mrs. Thing']
# change(names)
# print(names)

# n = names[:]
# print(n is names)
# print(n == names)

# def init(data):
# 	data['first'] = {}
# 	data['middle'] = {}
# 	data['last'] = {}

# # storage = {}
# # init(storage)
# # print(storage)

# def lookup(data, label, name):
# 	return data[label].get(name)

# def store(data, full_name):
# 	names = full_name.split()
# 	if len(names) == 2: names.insert(1, '')
# 	labels = 'first', 'middle', 'last'
# 	for label, name in zip(labels, names):
# 		people = lookup(data, label, name)
# 		if people:
# 			people.append(full_name)
# 		else:
# 			data[label][name] = [full_name]

# MyNames = {}
# init(MyNames)
# store(MyNames, 'magnus Lie Hetland')
# print(lookup(MyNames, 'middle', 'Lie'))

# store(MyNames, 'Robin Hood')
# store(MyNames, 'Robin Locksley')
# print(lookup(MyNames, 'first', 'Robin'))
# store(MyNames, 'Mr. Gumby')
# print(lookup(MyNames, 'middle', ''))

# def inc(x): return x + 1

# foo = 10
# foo = inc(foo)
# print(foo)

# def inc(x): x[0] = x[0] + 1
# foo = [10]
# inc(foo)
# print(foo)

# def hello_1(greeting, name):
# 	print('%s, %s!' % (greeting, name))

# def hello_2(name, greeting):
# 	print('%s, %s!' % (name, greeting))

# hello_1('Hello', 'World')
# hello_2('World', 'Hello' )

# hello_1(greeting='Hello', name='World')
# hello_2(greeting='World', name='Hello')

# def print_params(*params):
# 	print(params)

# print_params('Testing')
# print_params(1, 2, 3)

# def print_params2(title, *params):
# 	print(title)
# 	print(params)

# print_params2('Params', 1, 2, 3)
# print_params2('Nothing: ')

# def print_params3(**params):
# 	print(params)

# print_params3(x=1, y=2, z=3)

# def print_params_4(x, y, z=3, *pospar, **keypar):
# 	print(x, y , z)
# 	print(pospar)
# 	print(keypar)

# print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
# print_params_4(1, 2)

# def store(data, *full_names):
# 	for full_name in full_names:
# 		names = full_name.split()
# 		if len(names) == 2: names.insert(1, '')
# 		labels = 'first', 'middle', 'last'
# 		for label, name in zip(labels, names):
# 			people = lookup(data, label, name)
# 			if people:
# 				people.append(full_name)
# 			else:
# 				data[label][name] = [full_name]

# d = {}
# init(d)
# store(d, 'Luke Skywalker', 'Anakin Skywalker')
# print(lookup(d, 'last', 'Skywalker'))

# def story(**kwds):
# 	return 'Once upon a time, there was a %(job)s called %(name)s. ' %kwds
	
# def power(x, y, *others):
# 	if others:
# 		print('Received redundant parameters:', others)
# 	return pow(x, y)

# def interval(start, stop=None, step=1):
# 	'Imitates range() for step > 0'
# 	if stop is None:
# 		start, stop = 0, start
# 	result = []
# 	i = start
# 	while i < stop:
# 		result.append(i)
# 		i += step
# 	return result

# print(story(job='king', name='Gumby'))
# print(story(name='Sir Robin', job='brave knight'))
# params = {'job': 'language', 'name': 'Python'}
# print(story(**params))
# del params['job']
# print(story(job='stroke of genius', **params))
# print(power(2, 3))
# print(power(3, 2))
# print(power(y=3, x=2))
# params = (5,) * 2
# print(power(*params))
# print(power(3, 3, 'Hello, World'))
# print(interval(10))
# print(interval(1, 5))
# print(interval(3, 12, 4))
# print(power(*interval(3, 7)))

# x = 1
# scope = vars()
# print(scope['x'])
# scope['x'] += 1
# print(x)

# def foo(): x = 42

# x = 1
# foo()
# print(x)

# def combine(parameter): print(parameter + external)

# external = 'berry'
# combine('Shrub')

# def combine(parameter):
# 	print(parameter + globals()['parameter'])

# parameter = 'berry'
# combine('Shrub')

# global
# x = 1
# def change_global():
# 	global x
# 	x = x + 1

# change_global()
# print(x)

# create a func
# def multiplier(factor):
# 	def multiplyByFactor(number):
# 		return number*factor
# 	return multiplyByFactor

# double = multiplier(2)
# print(double(5))
# triple = multiplier(3)
# print(triple(3))
# print(multiplier(5)(4))

# factorial
# def factorial(n):
# 	result = n
# 	for i in range(1, n):
# 		result *= i
# 	return result

# def factorial(n):
# 	if n == 1:
# 		return 1
# 	else:
# 		return n * factorial(n-1)

# search
# def power(x, n):
# 	result = 1
# 	for i in range(n):
# 		result *= x
# 	return result

# def power(x, n):
# 	if n == 0:
# 		return 1
# 	else:
# 		return x * power(x, n-1)

# def search(sequence, number, lower=0, upper=None):
# 	if upper is None: upper = len(sequence) - 1
# 	if lower == upper:
# 		assert number == sequence[upper]
# 		return upper
# 	else:
# 		middle = (lower + upper) // 2
# 		if number > sequence[middle]:
# 			return search(sequence, number, middle+1, upper)
# 		else:
# 			return search(sequence, number, lower, middle)

# seq = [34, 67, 8, 123, 4, 100, 95]
# seq.sort()
# print(seq)
# print(search(seq, 34))
# print(search(seq, 100))

#map
# print(list(map(str, range(10))))
# print([str(i) for i in range(10)])

def func(x):
	return x.isalnum()

seq = ['foo', 'x41', '?!', '***']
print(list(filter(func, seq)))

print([x for x in seq if x.isalnum()])
print(list(filter(lambda x: x.isalnum(), seq)))