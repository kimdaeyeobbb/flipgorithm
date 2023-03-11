import math

n = int(input())
end = n
start = 0

# 이진 탐색
while(end >= start):
    mid = (start+end)//2
    if (mid**2 >= n):
        end = mid-1
    else:
        start = mid+1

print(start)
'''
부동소수점 참고자료

# 1
https://datascienceschool.net/01%20python/02.02%20%EB%B6%80%EB%8F%99%EC%86%8C%EC%88%98%EC%A0%90%20%EC%8B%A4%EC%88%98%20%EC%9E%90%EB%A3%8C%ED%98%95.html

# 2
https://dojang.io/mod/page/view.php?id=2466

# 3
https://docs.python.org/ko/3/tutorial/floatingpoint.html
'''