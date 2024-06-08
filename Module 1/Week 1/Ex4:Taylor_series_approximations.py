import math

def factorial(k):
    if k == 0:
        return 1
    result = 1
    for i in range(1, k + 1):
        result *= i
    return result

def taylor_sin(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i * x**(2*i + 1)) / factorial(2*i + 1)
    return result

def taylor_cos(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i * x**(2*i)) / factorial(2*i)
    return result

def taylor_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x**(2*i + 1)) / factorial(2*i + 1)
    return result

def taylor_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x**(2*i)) / factorial(2*i)
    return result

# Example usage
x = 3.14  # value for which to compute the series
n = 10  # number of terms in the series

print("Taylor series approximation of sin(x):", taylor_sin(x, n))
print("Taylor series approximation of cos(x):", taylor_cos(x, n))
print("Taylor series approximation of sinh(x):", taylor_sinh(x, n))
print("Taylor series approximation of cosh(x):", taylor_cosh(x, n))

assert round ( taylor_cos ( x =1 , n =10) , 2) ==0.54
print ( round ( taylor_cos ( x =3.14 , n =10) , 2) )

assert round ( taylor_sin ( x =1 , n =10) , 4) ==0.8415
print ( round ( taylor_sin ( x =3.14 , n =10) , 4) )

assert round ( taylor_sinh ( x =1 , n =10) , 2) ==1.18
print ( round ( taylor_sinh ( x =3.14 , n =10) , 2) )

assert round ( taylor_cosh ( x =1 , n =10) , 2) ==1.54
print ( round ( taylor_cosh ( x =3.14 , n =10) , 2) )