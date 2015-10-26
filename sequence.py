#an N-eleme tuple or sequence
#unpacking into a collection of N variables

p = (4, 5)
x, y = p
print (x)
print (y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print (name)
print (date)

name, shares, price, (year, mon, day) = data
print (name) 
print (year)
print (mon)
print (day)


#a mismatch in the number of elements, get an error

p = (4, 5)
x, y, z = p