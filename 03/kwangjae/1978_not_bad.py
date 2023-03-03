#40ms
import sys 
from math import sqrt
N = int(sys.stdin.readline().strip())
nums = map(int, sys.stdin.readline().strip().split())
def prime_counter(cnt, num): 
    if num==1:
        return cnt 
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            return cnt
    return cnt+1
cnt = 0
for num in nums:
    cnt = prime_counter(cnt,num)
print(cnt)