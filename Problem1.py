#Project Euler: Problem 1 (Complete)
#Problem Source: www.projecteuler.net/problem=1
#Find the sum of all the multiples of 3 or 5 below 1000.

print sum(
    i for i in range(1000) if not i % 3 or not i % 5
)
