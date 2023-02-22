import sys 
import math 
N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip(" ").split()))

def gcd(a,b): #math.gcd로 대체가능 
    for i in range(min(a,b),0, -1):
        if a % i == 0 and b % i == 0:
            return i 
if N==2: 
    gcd_ =gcd(nums[0], nums[1])
else: 
    gcd_ = gcd(gcd(nums[0], nums[1]), nums[2]) 
answer =set()
for i in range(1, int(gcd_**0.5)+1):
    if gcd_%i == 0:
        answer.add(i)
        answer.add(gcd_//i)
answer =sorted(answer)
print(*answer, sep="\n")