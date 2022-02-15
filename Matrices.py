'''
from numpy import *
A=matrix([5,6,7])
print(A)
B=matrix([[1],[2],[3],[4]])
print(B)
#C=identity(3)
C=eye(5)
print(C)
D=zeros((6,5))
print(D)
E=ones((4,5))
print(E)
F=diag((7,8,9))
print(F)

from numpy import *
A=matrix([[1,2],[3,4]])
B=matrix([[5,6],[7,8]])
print('A =',A)
print('B =',B)
print('A+B =',A+B)
print('A-B =',A-B)
print('A*A =',A*A)
print('A*B =',A*B)
print('B*A =',B*A)
print('B**4+A**3 =',B**4+A**3)
print('Inverse of A=',A.I)
print('1st row of A=',A[0])
print('2nd row of A=',A[1])
print('last column of B=',B[-1])


from numpy import *
A=matrix([[1,2,3],[4,5,6],[7,8,9]])
print('A =',A)
print('del_2nd_row_A=',delete(A,1,0))


from numpy import *
B=matrix([[4,5],[6,7]])
print('B =',B)
print('del_1st_col_B=',delete(B,0,1))


from numpy import *
C=matrix([[1,0,0],[1,1,1],[1,2,3]])
print('C =',C)
print('insert_2nd_row_C=',insert(C,1,[1,1,0],0))


from numpy import *
A=matrix([[1,7,1],[4,-2,1],[3,1,2]])
print('A =',A)
print('del_3rd_row_A=',delete(A,2,0))
print('del_1st_col_A=',delete(A,0,1))
print('del_last_col_A=',delete(A,2,1))

