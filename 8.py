# try:
# 	x = int(input('Enter the first number: '))
# 	y = int(input('Enter the second number: '))
# 	print(x//y)
# except ZeroDivisionError:
# 	print("The second number can't be zero!")

# class MuffledCalculator:
# 	muffled = False
# 	def calc(self, expr):
# 		try:
# 			return eval(expr)
# 		except (ZeroDivisionError, TypeError) as e:
# 			print(e)

# calculator = MuffledCalculator()
# print(calculator.calc('10/2'))

# calculator.muffled = True
# calculator.calc('10/0')

# try:
# 	print('A simple task')
# except:
# 	print('What? Something went wrong?')
# else:
# 	print('Ah... It went as planned.')

# while True:
# 	try:
# 		x = int(input('Enter the first number: '))
# 		y = int(input('Enter the second number: '))
# 		value = x/y
# 		print('x/y is ', value)
# 	except:
# 		print('Invalid input. Please try again.')
# 	else:
# 		break

# while True:
# 	try:
# 		x = int(input('Enter the first number: '))
# 		y = int(input('Enter the second number: '))
# 		value = x/y
# 		print('x/y is ', value)
# 	except Exception as e:
# 		print('Invalid input:', e)
# 		print('Please try again')
# 	else:
# 		break

# x = None
# try:
# 	x = 1/0
# finally:
# 	print('Cleaning up...')
# 	del x

try:
	1/0
except NameError:
	print('Unknown variable')
else:
	print('That went well!')
finally:
	print('Cleaning up.')