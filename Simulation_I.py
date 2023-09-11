
from random import *
from time import *
a = randrange(1,3)
c = randrange(1,5)
ran = [randrange(0,a+1) for i in range(c)]
ran2 = [randrange(0,a+1) for i in range(c)] + ran
ran3 = [randrange(0,a+1) for i in range(c)] + ran2
ran4 = [randrange(0,a+1) for i in range(c)] + ran3
ran5 = [randrange(0,a+1) for i in range(c)] + ran4
ran6 = [randrange(0,a+1) for i in range(c)] + ran5
ran7 = [randrange(0,a+1) for i in range(c)] + ran6
ran8 = [randrange(0,a+1) for i in range(c)] + ran7
ran9 = [randrange(0,a+1) for i in range(c)] + ran8
ran10 = [randrange(0,a+1) for i in range(c)] + ran9
ran11= [randrange(0,a+1) for i in range(c)] + ran10
ran12= [randrange(0,a+1) for i in range(c)] + ran11
ran13= [randrange(0,a+1) for i in range(c)] + ran12
print("범위 0 ~",a)
sleep(5)
n = 0.7
print(ran)
sleep(n)
print(ran2)
sleep(n)
print(ran3)
sleep(n)
print(ran4)
sleep(n)
print(ran5)
sleep(n)
print(ran6)
sleep(n)
print(ran7)
sleep(n)
print(ran8)
sleep(n)
print(ran9)
sleep(n)
print(ran10)
sleep(n)
print(ran11)
sleep(n)
print(ran12)
sleep(n)
print(">>",ran13,"<<")
sleep(10)
print(choice(ran13))
