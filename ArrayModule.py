#comment on Array module

from array import *
a= array('d',[1,2,34,5,6,7])
print(a)
#comment on length of an array
print(len(a))
print(a[2])
#Adding single character
a.append(3.14)
print(a)
#adding multiple character
a.extend([1.2,2.1,3.2])
print(a)
#adding character on the basis of indexing
a.insert(2,1.1)
print(a)


#Pop out Character

a.pop()
print(a)

a.pop(8)
print(a)
#Removing a Character
a.remove(6.0)
print(a)

