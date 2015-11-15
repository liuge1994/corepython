__metaclass__ = type

# class Person:

# 	def setName(self, name):
# 		self.name = name

# 	def getName(self):
# 		return self.name

# 	def greet(self):
# 		print("Hello, world! I'm %s." % self.name)

# foo = Person()
# bar = Person()
# foo.setName('Luke Skywalker')
# bar.setName('Anakin Skywalker')
# foo.greet()
# bar.greet()

# class Class:
# 	def method(self):
# 		print('I have a self!')

# def function():
# 	print("I don't...")

# instance = Class()
# instance.method()
# instance.method = function
# instance.method()

# class Bird:
# 	song = 'Squaawk!'
# 	def sing(self):
# 		print(self.song)

# bird = Bird()
# bird.sing()
# birdsong = bird.sing
# birdsong()

# class MemberCounter:
# 	member = 0
# 	def init(self):
# 		MemberCounter.member += 1

# m1 = MemberCounter()
# m1.init()
# print(MemberCounter.member)
# m2 = MemberCounter()
# m2.init()
# print(MemberCounter.member)
# print(m1.member)
# print(m2.member)

class Filter:
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
	def init(self):
		self.blocked = ['SPAM']

f = Filter()
f.init()
print(f.filter([1, 2, 3]))

s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))

print(issubclass(SPAMFilter, Filter))
print(issubclass(Filter, SPAMFilter))
print(SPAMFilter.__bases__)
print(Filter.__bases__)

s = SPAMFilter()
print(isinstance(s, SPAMFilter))
print(isinstance(s, Filter))
print(isinstance(s, str))
print(s.__class__)
print(type(s))
