import time

def gcd(a,b):
    best=0
    for d in range(1,a+b):
        if a%d==0 and b%d==0:
            best=d
    return best
    
c=time.time()
print(gcd(484444,884444))
print(f"time taken {time.time()-c}")

def gcd2(a,b):
    if b==0:
        return a
    else:
        a1=a-(a//b)*b
        return gcd2(b,a1)
c1=time.time()
print(gcd2(375,234))
print(f"Time takem {time.time()-c1}")