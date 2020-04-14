#Comment on Python
#modules
#nametuple

from collections import namedtuple

a= namedtuple('courses','name,technology')
s= a('Big Data','Python')
print(s)

#comment on Python
#Modules
#Deque
from collections import deque

a=(['R','A','J','U'])
d=deque(a)
print(d)

d.append('Python')
print(d)

d.appendleft('AI')
print(d)

d.pop()
print(d)

d.popleft()
print(d)
