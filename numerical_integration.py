# -*- coding: utf-8 -*-
"""Numerical Integration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1leTiYChk1icoTySeGHw3yu4rHKyqtjEh

Trapezoidal Rule
"""

def trapezoidal(f,a,b,n):
  l1=[]
  h=float((b-a)/n)
  
  for i in range(1,n):
    k=a+i*h
    l1.append(f(k))
  exp2=(f(a)+f(b))+(2*sum(l1))
  result=(h/2)*exp2
  return(result)
  

from math import *
def f(x):
  return (x+1)**2
  
print(trapezoidal(f,0,2,8))

from math import *
def f(x):
  return (x+1)**2
print(trapezoidal(f,0,2,100))

"""Simpsons(1/3)rd Rule"""

def simpsons13(f,a,b,n):
  even=[]
  odd=[]
  h=float(b-a)/n
  result=f(a)+f(b)
  for i in range(1,n):
    k=a+i*h
    if i%2==0:
      even.append(f(k))
    else:
      odd.append(f(k))
  exp=result+(4*sum(odd)+(2*sum(even)))
  final=exp*(h/3)
  return final

from math import *
def f(x):
  return sqrt(1+x**3)
print(simpsons13(f,0,5,10))

"""Simpsons (3/8)th Rule"""

def simpsons38(f,a,b,n):
  M_3=[]
  M_NOT3=[]
  h=float(b-a)/n
  result=f(a)+f(b)
  for i in range(1,n):
    k=a+i*h
    if i%3==0:
      M_3.append(f(k))
    else:
      M_NOT3.append(f(k))
  exp=result+(3*sum(M_NOT3)+(2*sum(M_3)))
  final=exp*((3*h)/8)
  return final

from math import *
def f(x):
  return x**3+2*x**2-8
print(simpsons38(f,0,5,10))