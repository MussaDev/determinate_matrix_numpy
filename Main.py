import numpy as np

def sum (a,b):
    c = a+b
    return c

def mnoj (a, b):
    c = a.dot(b)
    return c

def trans(a):
    a = a.transpose()
    return a

def det (a):
    c = np.linalg.det(a)
    return c

A = np.array([[1,2,3],
     [4,6,8,],
     [4,7,3]])
B = np.array([[4,0,8],
     [1,5,9,],
     [25,14,7]])

print ("Матрица А")
print (A,"\n")

print ("Матрица B")
print (B,"\n")

print ("Сумма матриц А и В")
print (sum(A,B),"\n")

print ("Произведение матри А и В")
print (mnoj(A,B), '\n')

print ("Транспонированная матрица от А")
print (trans(A), '\n')

print ("Определитель матрицы А")
print (det(A), "\n")


