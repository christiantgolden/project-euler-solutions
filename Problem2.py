#Project Euler: Problem 2 (Complete)
#Problem Source: www.projecteuler.net/problem=2
#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.

fibList = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

while fibList[-1] + fibList[-2] <= 4000000:
    fibList.append(fibList[-1] + fibList[-2])

print sum(
    i for i in fibList if not i % 2
)
