# 1110번 더하기 사이클

n = int(input())
init_n = n

def make_newnum(n):   # 새로운 수를 만드는 함수
    sum_each = (n // 10) + (n % 10)
    newnum = ((n % 10) * 10) + (sum_each % 10)
    return newnum

# 사이클 1은 따로 먼저 해주기
n =  make_newnum(n)
cycle = 1

# 사이클 2부터 반복
while n != init_n:
    n = make_newnum(n)
    cycle += 1

print(cycle)