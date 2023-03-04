#44ms
from sys import stdin

N, K = map(int, stdin.readline().strip().split())
def prime_sieve(N, K):
    
    arr =[True for i in range(N+1)]
    arr[0], arr[1]=False, False
    cnt=0 
    for i in range(2,N+1):
        if arr[i]==True:
            j=1
            while i*j<N+1:
                if arr[i*j]==True: 
                    cnt+=1
                arr[i*j]=False
                if cnt==K:
                    return i*j 
                j+=1
print(prime_sieve(N,K))    
    