# 1978번 소수 찾기

n = int(input())

num_list = list(map(int, input().split()))

count = n

for i in num_list:
    if i == 1:
        count -= 1   # 1이면 전체 count에서 1 차감
    else:
        for j in range(2, int(i**(1/2))+1): # 2 ~ 자기 자신의 제곱근까지 범위 반복
            if i % j == 0:                  # 나누어 떨어지는 수가 있으면
                count -= 1                  # 전체 count에서 1 차감 후
                break                       # 반복 중단

print(count)