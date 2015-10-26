#list order
#set don't care about the order

from collections import defaultdict

# d = {
# 	'a' : [1, 2, 3],
# 	'b' : [4, 5]
# }

# e = {
# 	'a' : {1, 2, 3},
# 	'b' : {4, 5}
# }

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

c = defaultdict(set)
c['a'].add(1)
c['a'].add(2)
c['b'].add(4)

print(c)