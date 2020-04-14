#ChainMap Modules
#comment on Python
#Joining Two or more array
from collections import ChainMap

a={1:'Nepal', 2:'information'}
b= {3: 'Technology', 4: 'Country'}

c=ChainMap(a,b)
print(c)