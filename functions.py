
A='number'
print(type(A))
b=31.25
print(type(b))
c=8+4j
print(type(c))
d=49
print(type(d))
e=(1,2,3,4,5)
print(type(e))
f=[10,20,30,-40,'dog']
print(type(f))




print(float(31))
print(int(31.4))
print(str(3.14))
print(int('sumit'))



def add_numbers(x,y):
	sum = x+y
	return sum

x=int(input("Enter x: "))
y=int(input("Enter y: "))

print(add_numbers(x,y))




def f(x):
        return x**2
print(f(5))




def divisors(x):
        for i in range(1,x+1):
                if x%i==0:
                        print(i,end=',')
divisors(20)
                        



def f(x):
        return x+2
def g(x):
        return 2*x
print(f(g(2)))
print(g(f(2)))



def p(x):
        return 2*x
def q(x):
        return x+1
print(p(q(10)))

