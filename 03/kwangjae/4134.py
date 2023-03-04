import sys 
import math
N = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))
target = int(sys.stdin.readline().strip())
answer =[]
for num in nums:
    if num%target!=0 and target%num!=0:
        answer.append(num)
answer =sum(answer)/len(answer)

print('%0.6f'%(answer))
