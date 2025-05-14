import math
def pi(n):
    r=0
    r1=1
    s=-1
    for k in range(n) :
        s=s*(-1)
        r1=r1*(1/2-k)
        r=r+(1/math.factorial(k))*r1*s*(1/2)
