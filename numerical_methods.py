# -*- coding: utf-8 -*-
"""Numerical methods.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZX4hNf5xwCY5vvxSIvSNFC0rZWKWjZeE

Find the root of the equation by newton raphson method.
"""

def newtonraphson(f,df,x0,e):
  step=1
  condition=True
  while condition:
    if df(x0)==00:
      print('Divided by zero error!')
      break
    x1=x0-(f(x0)/df(x0))
    print('Iteration=',step,'x1=',x1,'and f(x1)=',f(x1))
    x0=x1
    step=step+1
    condition=abs(f(x1))>e
    print('Required root is:',x1)
from math import *
def f(x):
  return x**5 - 5*x + 1
def df(x):
  return 5*x**4 - 5
newtonraphson(f,df,-0.5,0.00001)

def f(x):
  return x**3
def df(x):
  return 3*x**2
newtonraphson(f,df,0.7,0.00001)

def f(x):
  return x**3 - 10*x**2 + 5
def df(x):
  return 3*x**2 - 20*x
newtonraphson(f,df,0.7,0.00001)

def f(x):
  return cos(x)
def df(x):
  return -sin(x)
newtonraphson(f,df,1.1,0.00001)

"""Find the root of the equation by regular falsi or false postion method."""

def falseposition(f,x0,x1,e):
  if(f(x0)*f(x1))>0:
    print('given guess values do not bracker the root')
    print('try again with different guess values')
  else:
    step=1
    condition=True
    while condition:
      x2=((x0*f(x1))-(x1*f(x0)))/(f(x1)-f(x0))
      print('Iteration=',step,'x2=',x2,'and f(x2)=',f(x2))
      if(f(x0)*f(x2))>0:
        x1=x2
      else:
        x0=x2
      step=step+1
      condition=abs(f(x2))>e
    print('Required root is:',x2)
from math import *
def f(x):
  return x**3-x-1
falseposition(f,1,2,0.00001)

from math import *
def f(x):
  return exp(x)-3*x
falseposition(f,0,1,0.00001)

from math import *
def f(x):
  return log(x)-cos(x)
falseposition(f,1,2,0.00001)