#comment on python
#Counter modules
#Count a number of an element
from collections import Counter

a=[1,1,1,1,1,1,13,3,3,33,3,4,4,4,4,4,47,777,7,7,7,7]
c=Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())

sub={1:3, 33:1}
print(c.subtract(sub))
print(c)

print(c.most_common())