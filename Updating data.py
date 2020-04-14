#Accessing a data
#modules

from collections import defaultdict

my_dict={'Ram': '001','Raj': '002','Hari': '003'}

print(my_dict)

print(my_dict.values())


for x in my_dict:
    print(x)

    for x in my_dict.values():
        print(x)


for x,y in my_dict.items():
    print(x,y)

    #updating the data
    #modules


    my_dict['Ram']='004'
    my_dict['Hari']='001'
    my_dict['Charlie']='005'
    print(my_dict)