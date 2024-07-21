from utils import *

# def intersection (a,b)


list1 = sieve(1,5,40)
list2 = sieve(2, 7, 50)
list3 = sieve(3, 4, 50)

a = list(set(list1).intersection(list2))


print(a)

