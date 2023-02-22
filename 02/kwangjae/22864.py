import sys
def max_mul(a,b):
    mu = []
    for i in range(1,max(a,b)+1):
        if a%i ==0 and b%i == 0:
            mu.append(i)
    return max(mu)

def min_mul(a,b):
    mi =[]
    result = a*b//max_mul(a,b)
    return result 
     

a,b = map(int,sys.stdin.readline().strip().split(' '))

print(f'{max_mul(a,b)}\n{min_mul(a,b)}')