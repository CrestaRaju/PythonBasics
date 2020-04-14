#removing Data
#modules

from collections import defaultdict

#using pop function for removing data
my_dict={'raju':'123','raj':'456','rahul':'789'}
print(my_dict)

my_dict.pop('raju')
print(my_dict)

my_dict.popitem()
print(my_dict)

#using del function for removing data

my_dict={'raju':'123','raj':'456','rahul':'789'}

del my_dict['raj']
print(my_dict)




