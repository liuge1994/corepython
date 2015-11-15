# class NewStyle(object):
# 	pass

# class OldStyle:
# 	pass


# class FooBar:
# 	def __init__(self, value=42):
# 		# self.somevar = 42
# 		self.somevar = value

# f = FooBar()
# print(f.somevar)

# f = FooBar('This is a constructor argument')
# print(f.somevar)

# class A:
# 	def hello(self):
# 		print("Hello, I'm A.")

# class B(A):
# 	def hello(self):
# 		print("Hello, I'm B.")

# a = A()
# b = B()
# print(a.hello())
# print(b.hello())

# class Bird:
# 	def __init__(self):
# 		self.hungry = True

# 	def eat(self):
# 		if self.hungry:
# 			print('Aaaah...')
# 			self.hungry = False
# 		else:
# 			print('No, thanks!')

# # b = Bird()
# # b.eat()
# # b.eat()

# class SongBird(Bird):
# 	def __init__(self):
# 		Bird.__init__(self)
# 		self.sound = 'Squawk!'
# 	def sing(self):
# 		print(self.sound)

# sb = SongBird()
# sb.sing()
# sb.eat()
# sb.eat()

# __metaclass__ = type

# class Bird:
# 	def __init__(self):
# 		self.hungry = True
# 	def eat(self):
# 		if self.hungry:
# 			print('Aaaah...')
# 			self.hungry = False
# 		else:
# 			print('No, thanks!')

# class SongBird(Bird):
# 	def __init__(self):
# 		super(SongBird, self).__init__()
# 		self.sound = 'Squawk!'
# 	def sing(self):
# 		print(self.sound)

# sb = SongBird()
# sb.sing()
# sb.eat()
# sb.eat()

# def checkIndex(key):
# 	if not isinstance(key, int): raise TypeError
# 	if key<0: raise IndexError

# class ArithmeticSequence:
# 	def __init__(self, start=0, step=1):
# 		self.start = start
# 		self.step = step
# 		self.changed = {}

# 	def __getitem__(self, key):
# 		checkIndex(key)
# 		try: return self.changed[key]
# 		except KeyError:
# 			return self.start + key*self.step

# 	def __setitem__(self, key, value):
# 		checkIndex(key)
# 		self.changed[key] = value

# s = ArithmeticSequence(1, 2)
# print(s[4])
# s[4] = 2
# print(s[4])
# print(s[5])

# class CounterList(list):
# 	def __init__(self, *args):
# 		super(CounterList, self).__init__(*args)
# 		self.counter = 0
# 	def __getitem__(self, index):
# 		self.counter += 1
# 		return super(CounterList, self).__getitem__(index)

# cl = CounterList(range(10))
# print(cl)

# cl.reverse()
# print(cl)

# del cl[3:6]
# print(cl)

# print(cl.counter)
# print(cl[4] + cl[2])
# print(cl.counter)

# class Rectangle:
# 	def __init__(self):
# 		self.width = 0
# 		self.height = 0
# 	def setSize(self, size):
# 		self.height = size
# 		self.width = size
# 	def getSize(self):
# 		return self.width, self.height


# r = Rectangle()
# r.width = 10
# r.height = 5
# print(r.getSize())
# r.setSize((150, 100))
# print(r.width)

# __metaclass__ = type
# class Rectangle:
# 	def __init__(self):
# 		self.width = 0
# 		self.height = 0
# 	def setSize(self, size):
# 		self.width = size
# 		self.height = size
# 	def getSize(self):
# 		return self.width, self.height

# 	size = property(getSize, setSize)

# r = Rectangle()
# r.width = 15
# r.height = 5
# print(r.size)
# r.size = 150, 100
# print(r.width)

# __metaclass__ = type

# class MyClass:
# 	def smeth():
# 		print('This is a static method')
# 	smeth = staticmethod(smeth)

# 	def cmeth(cls):
# 		print('This is a class method of', cls)
# 	cmeth = classmethod(cmeth)

# MyClass.smeth()
# MyClass.cmeth()

# class Rectangle:
# 	def __init__(self):
# 		self.width = 0
# 		self.height = 0
# 	def __setattr__(self, name, value):
# 		if name == 'size':
# 			self.width, self.height = value
# 		else:
# 			self.__dict__[name] = value
# 	def __getattr__(self, name):
# 		if name == 'size':
# 			return self.width, self.height
# 		else:
# 			raise AttributeError

# __metaclass__ = type

# class MyClass:

# 	@staticmethod
# 	def smeth():
# 		print('This is a static method')

# 	@classmethod
# 	def cmeth(cls):
# 		print('This is a class method of', cls)

# MyClass.smeth()
# MyClass.cmeth()

# class Rectangle:
# 	def __init__(self):
# 		self.width = 0
# 		self.height = 0
# 	def __setattr__(self, name, value):
# 		if name == 'size':
# 			self.width, self.height = value
# 		else:
# 			self.__dict__[name] = value
# 	def __getattr__(self, name):
# 		if name == 'size':
# 			return self.width, self.height
# 		else:
# 			raise AttributeError
# 			
# class Fibs:
# 	def __init__(self):
# 		self.a = 0 
# 		self.b = 1
# 	def __next__(self):
# 		self.a, self.b = self.b, self.a + self.b
# 		return self.a
# 	def __iter__(self):
# 		return self

# fibs = Fibs()
# for f in fibs:
# 	if f > 1000:
# 		print(f)
# 		break

# class TestIterator:
# 	value = 0
# 	def __next__(self):
# 		self.value += 1
# 		if self.value > 10: 
# 			raise StopIteration
# 		return self.value
# 	def __iter__(self):
# 		return self

# ti = TestIterator()
# print(list(ti))

# def flatten(nested):
# 	for sublist in nested:
# 		for element in sublist:
# 			yield element

# nested = [[1, 2], [3, 4], [5]]
# for num in flatten(nested):
# 	print(num)

# print(list(flatten(nested)))

# def flatten(nested):
# 	try:
# 		for sublist in nested:
# 			for element in flatten(sublist):
# 				yield element
# 	except TypeError:
# 		yield nested

# print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))

# def flatten(nested):
# 	try:
# 		try: nested + ''
# 		except TypeError: pass
# 		else: raise TypeError
# 		for sublist in nested:
# 			for element in flatten(sublist):
# 				yield element
# 	except TypeError:
# 		yield nested

# print(list(flatten(['foo', ['bar', ['baz']]])))

# def flatten(nested):
# 	result = []
# 	try:
# 		try:
# 			nested + ''
# 		except TypeError:
# 			pass
# 		else: raise TypeError
# 		for sublist in nested:
# 			for element in flatten(sublist):
# 				result.append(element)
# 	except TypeError:
# 		result.append(nested)
# 	return result
def conflict(state, nextX):
	nextY = len(state)
	for i in range(nextY):
		if abs(state[i]-nextX) in (0, nextY-i):
			return True
	return False

def queens(num, state=()):
	for pos in range(num):
		if not conflict(state, pos):
			if len(state) == num-1:
				yield (pos,)
			else:
				for result in queens(num, state + (pos,)):
					yield (pos,) + result

def prettyprint(solution):
	def line(pos, length=len(solution)):
		return '. ' * (pos) + 'X' + '. ' * (length-pos-1)
	for pos in solution:
		print(line(pos))
# print(list(queens(4, (1, 3, 0))))

a = len(list(queens(8)))
print(a)

# for solution in queens(8):
# 	print(solution)

prettyprint(list(queens(8)))
