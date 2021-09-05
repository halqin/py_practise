def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial  *= i
    return print(factorial)
# fact(3)

def triangle(n):
    for i in range(1,n+1):
        for j in range(i):
            print ('*',end=" "),
        print()
# triangle(4)

def triangle_inv(n):
    for i in range(1,n+1):
        for j in range(2*(i-1)):
            print(" ")
        for k in range():
            print("*",end=" ")

# triangle_inv(4)

def triangle_inv2(n):
    for i in range(n, 0, -1):
        for j in range(n-i):
            print("_")
        for k in range(2*i-1):
            print("*", end=" ")
        print()
# triangle_inv2(4)


def array_inv(arr):
    
    len_ = len(arr)
    new_arr = [1]*len_
    for i in range(len_): 
        new_arr[len_-i-1] = arr[i]
    return print(new_arr)
#array_inv([1,2,3])

def reverse1(a):
    N = len(a)
    for i in range(N//2):
        k = N - i -1 
        a[i], a[k] = a[k],a[i]
    return a
b= [1,2,3]
reverse1(b)
print(b)