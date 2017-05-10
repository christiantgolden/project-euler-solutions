#Project Euler: Problem 3 (Complete)
#Problem Source: www.projecteuler.net/problem=3
#What is the largest prime factor of the number 600851475143 ?

import math
import time

start = time.time()

a = 0
prime_list = [2, 3]
index = prime_list[-1] + 2
y = int(raw_input("Enter your num: "))
z = math.sqrt(y)
while index < z:
    if index % prime_list[a] != 0:
        if prime_list[a] ** 2 > index:
            prime_list.append(index)
            a = 0
            index += 2
        else:
            a += 1
    else:
        index += 2
        a = 0

number = y
factorList = []
for i in prime_list:
    while y % i == 0:
        factorList.append(i)
        y = y/i
if y > 1:
    factorList.append(y)

print "The prime factors of", number, "are:", factorList
print "The largest prime factor of", number, "is", max(factorList)
print (time.time() - start)
