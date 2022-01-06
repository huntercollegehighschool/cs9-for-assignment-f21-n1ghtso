"""
******
PART 2
******
Write a program that asks the user to enter a positive integer n. The program will then print the sum of the first n positive cubes.

For example, if the user types in 4, the program should print 100 (since 1^3 + 2^3 + 3^3 + 4^3 = 100).
"""

n = int(input("Enter number for n: "))

sum = 0
product = 0

for i in range(n, 0, -1):
  product = i * i * i
  sum += product
  product = 0

print(sum)