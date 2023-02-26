#52ms
import sys 
from math import gcd 

N = int(sys.stdin.readline().strip())

def lcm(a,b):
    return (a*b)//gcd(a,b)

for i in range(N):
    a,b = map(int, sys.stdin.readline().strip().split())
    print(lcm(a,b))