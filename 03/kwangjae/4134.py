import sys 
import math
N = int(sys.stdin.readline().strip())

def is_prime(n): 
    for i in range(2,int(math.sqrt(n))+1 ):
        if n%i ==0:
            return False
    return True 

for i in range(N):
    num = int(sys.stdin.readline().strip())
    if num ==0 or num ==1:
        print(2)
    else: 
        while True:
            if is_prime(num)==True:
                print(num)
                break 
            num+=1
