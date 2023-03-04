#44ms 
import sys

M = int(sys.stdin.readline().strip())
N= int(sys.stdin.readline().strip())

def prime_sieve(M,N):
    
    arr =[True for i in range(N+1)]
    arr[0], arr[1]=False, False
    for i in range(2,N+1):
        if arr[i]==True:
            j=2
            while i*j<N+1:
                arr[i*j]=False
                j+=1
    return arr  

prime_num = [num[0] for num in enumerate(prime_sieve(M,N)) if num[1]==True and num[0]>=M ] 

if len(prime_num)!=0:
    print(sum(prime_num))
    print(min(prime_num))
else: 
    print(-1)