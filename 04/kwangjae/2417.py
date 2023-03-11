import sys 
import math 
num = int(sys.stdin.readline().strip())
mid  =num//2 
min_, max_ = 0, num
for i in range(0,10):
    sqr = mid**2
    print(mid)
    if sqr>=num and (mid-1)**2<num:
        break 
    if sqr ==num:
        break
    elif sqr>num:
        max_=mid
        mid=(mid-min_)//2 
        
     
    elif sqr<num:
        min_=mid
        mid = (max_-mid)//2
        
print(mid)     
    
        