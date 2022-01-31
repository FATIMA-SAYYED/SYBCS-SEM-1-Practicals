# -*- coding: utf-8 -*-
"""Matrices2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EbHVOKKcWjJvyXf5l8Qh8HUZHfsxbwAb
"""

import numpy
import scipy.linalg
from numpy import *
from scipy import *
A=matrix([[1,2,4],[1,6,2],[1,1,0]])
print(A)
linalg.det(A)

B=matrix([[1,2],[3,4]])
print('B=',B)
print('Transpose of B=',B.T)
print('Determinanat of B=',linalg.det(B))

from numpy import *
from scipy import *
C=Matrix([[7,8],[9,10]])
print('C=',C)
print('trace=',trace(C))
print('rank=',linalg.matrix_rank(C))

from numpy import *
from sympy import *
D=Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(D)
D.nullspace()
D.columnspace()
print('rref=',D.rref())

x, y, z = symbols("x, y, z")
>>> A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
>>> b = Matrix([3, 6, 9])
linsolve((A, b), [x, y, z])

x, y, z = symbols("x, y, z")
A=Matrix([[1,1,1],[1,-1,1],[1,-1,-1]])
b=Matrix([3,1,-1])
linsolve((A, b), [x, y, z])

A=Matrix([[1,1],[1,-1]])
B=Matrix([3,1])
print('sol, params =' ,A.gauss_jordan_solve(B))

x,y,z=symbols("x,y,z")
AB=Matrix([[4,5,6,15],[7,8,9,24],[1,1,2,4]])
solve_linear_system_LU(AB, [x,y,z])