# class MyData(object):
# 	pass

# mathObj = MyData()
# mathObj.x = 4
# mathObj.y = 5
# print(mathObj.x + mathObj.y)
# print(mathObj.x * mathObj.y)

# class C(object):
# 	foo = 100

# print(C.foo)
# C.foo = C.foo + 1
# print(C.foo)

# class MyClass(object):
# 	def myNoActionMethod(self):
# 		pass

# mc = MyClass()
# mc.myNoActionMethod()

# # myNoActionMethod()

# class MyClass(object):
# 	'MyClass class definition'
# 	myVersion = '1.1'           # static data 
# 	def showMyVersion(self):    # method 
# 	    print(MyClass.myVersion)
# print(dir(MyClass))
# dir(MyClass)
# print(MyClass.__dict__)

# print(MyClass.__name__)
# print(MyClass.__doc__)
# print(MyClass.__bases__)
# print(MyClass.__dict__)
# print(MyClass.__module__)
# print(MyClass.__class__)

# stype = type('What id your quest?')
# print(stype)
# print(stype.__name__)
# print(type(3.14))
# print(type(3.14).__name__)

# class C(P):
# 	def __init__(self):
# 		print('initialized')
# 	def __del__(self):
# 		P.__del__(self)

# c1 = C()
# c2 = c1
# c3 = c1
# print(id(c1), id(c2), id(c3))

# del c1
# del c2
# # del c3

# class InstCt(object):
# 	count = 0

# 	def __init__(self):
# 		InstCt.count += 1

# 	def __del__(self):
# 		InstCt.count -= 1

# 	def howMany(self):
# 		return InstCt.count

# a = InstCt()
# b = InstCt()
# print(b.howMany())
# print(a.howMany())
# del b
# print(a.howMany())
# del a 
# print(InstCt.count)

class HotelRoomCale(object):
	'Hotel room rate calculator'

	def __init__(self, rt, sales=0.085, rm=0.1):
		'''HotelRoomCale default arguments:
		sales tax == 8.5% and room tax == 10%'''
		self.salesTax = sales
		self.roomTax = rm 
		self.roomRate = rt

	def calcTotal(self, days=1):
		'calculate total: default to daily rate'
		daily = self.roomRate * (1.0 + self.roomTax + self.salesTax)
		return float(days) * daily

sfo = HotelRoomCale(299)
print(sfo.calcTotal())
print(sfo.calcTotal(2))
sea = HotelRoomCale(189, 0.089, 0.058)
print(sea.calcTotal())
print(sea.calcTotal(4))
wasWkDay = HotelRoomCale(169, 0.045, 0.02)
wasWkEnd = HotelRoomCale(119, 0.045, 0.02)
print(wasWkDay.calcTotal(5) + wasWkEnd.calcTotal())
print(wasWkDay.calcTotal(5))
print(wasWkEnd.calcTotal())
a = wasWkDay.calcTotal(5) + wasWkEnd.calcTotal()
print(a)
