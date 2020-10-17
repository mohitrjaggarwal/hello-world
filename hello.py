#time
import time
import calendar


r = time.localtime(time.time())
t = calendar.month(2020,10)
print(r)

def printinfo( *variable):


   for var in variable:
      print(var)
   return

mylist = [1,2,3,4,5,6,7,9]
printinfo( 10 ,mylist)
printinfo( 70, 60, 50 )
print(dir(time))
print(time.clock())

class Swaraj:
   'documentation of class'
   a = 5
   b = 6
   def __init__(self,b= 6):
      b = 5
   def func(self):
      print("this is great")
   def __repr__(self):
      return 'namee'

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)


s =Swaraj()
print(s)
print(s.__dict__)

import re
nameage = ''' i m Mohit with age 19 
                      i m Rohan with age 20'''

ages =   re.findall(r'\d{1,3}' , nameage)
names  = re.findall(r'[A-Z][a-z]*',nameage)
print(names)
mydict = dict()
x = 0
for name in names:
   mydict[name] = ages[x]
   x+=1
print(mydict)


#re.search

items = "flag emblem parliament redfort"
regex = re.compile("redfort")
new = regex.sub("somnath",items)
print(new)

num = "123 24356 52 54 15432112543 15 423339877"
r = re.findall('\d{3}',num)
print(r)


