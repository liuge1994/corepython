##problem
##You want to keep a limited history of the last few itrms seen during iteration or during some other kind of processing

from collections import deque

# def search(lines, pattern, history=5):     
# 	previous_lines = deque(maxlen =history)     
# 	for line in lines:         
# 		if pattern in line:             
# 			yield line, previous_lines         
#         previous_lines.append(line)

# Example use on a file 
#if __name__ == '__main__':     
#	with open('somefile.txt')as f:         for line, prevlines in search(f, 'python',
#5): for pline in prevlines:                 print(pline, end='') print(line,
#end='')             print('-'*20)

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
print(q.pop())
print(q)
print(q.popleft())
print(q)

# Creating New iteration Patterns with Generators

def frange(start, stop, increment):
	x = start
	while x < stop:
		yield x
		x += increment
for n in frange(0, 4, 0.5):
	print(n)


print (list(frange(0, 1, 0.125)))

def countdown(n):
	print('Starting to count from', n)
	while n > 0:
		yield n
		n -= 1
	print('Done!')

# Create the generator, notice no output appears

c = countdown(3)
print (c)

#Run to first yield and emit a value
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))



