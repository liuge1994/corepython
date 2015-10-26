records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
]

def do_foo(x, y):
	print('foo', x, y)

def do_bar(s):
	print('bar', s)

for tag, *args in records:
	if tag == 'foo':
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)



line = 'nobody:*:-2:-2:Unprivileged Ueser:/var/empty:/uer/bin/false'

unname, *fields, homedir, sh = line.split(':')
print (unname)
print (homedir)
print (sh)


#_ = ingore

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print (name)
print (year)


#head and tail

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)


#some kind of clever recursive algorithm
def sum(items):
	head, *tail = items
	return head + sum(tail) if tail else head

print (sum(items))
