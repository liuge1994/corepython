#Unpacking actually wroks with any object 
#includes strings, files, iterators, and generators

s = 'Hello'
a, b, c, d, e = s
print (a)
print (b)
print (e)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data

print (shares)
print (price)
