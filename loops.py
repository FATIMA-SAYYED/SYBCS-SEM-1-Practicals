
from math import pi, pow
r=int(input("Enter the radius"))
A=pi*pow(r,2)
print("Area of a circle is ",A)

print("***********************************************")

a=int(input("enter first integer"))
b=int(input("enter second integer"))
print("addition is ",a+b)

print("***********************************************")

x=int(input('enter an integer'))
if x>0:
	print("positive")
else:
	print("negative")

print("***********************************************")

x=int(input("enter an integer "))
r=x%2
if r==0:
	print("even")
else:
	print("odd")

print("***********************************************")
import math
from math import sqrt,log
x=int(input("Enter an integer"))
if x>0:
	print("square root is ",sqrt(x))
	print("log is ",log(x))
else:
	print("Number is negative")
print("***********************************************")

i=20
while i>=1:
	print(i)
	i=i-1

print("***********************************************")

x=int(input("Enter positive integer"))
i=1
while i<=10:
	print(x*i)
	i=i+1

print("***********************************************")
x=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for i in x:
	print(i)

print("***********************************************")

for i in range(21):
	print(i)

print("***********************************************")

for i in range (31,51,2):
	print(i)

print("***********************************************")
for i in range (100,201,1):
	if i%7==0:
		print(i)

print("***********************************************")

