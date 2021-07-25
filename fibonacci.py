import time

def fibonacci(n):
    if n<=1:
        return n
    else :
        return (fibonacci(n-1)+fibonacci(n-2))
c=time.time()
fib=[]
for i in range(35):
    fib.append(fibonacci(i))
print(fib)
print(f"Recustive time {time.time()-c}")

def fibonacci2(n):
    arr=[]
    for i in range(n):
        if i == 0:
            arr.append(0)
        elif i == 1:
            arr.append(1)
        else:
            arr.append(arr[i-1]+arr[i-2])
    return arr
c2=time.time()
print(fibonacci2(35))
print(f"Better ALG time {time.time()-c2}")