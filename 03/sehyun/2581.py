# 2581번 소수

M = int(input())
N = int(input())

num_list = []

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**(1/2))+1):
        if i % j == 0:
            break
    else:
        num_list.append(i)  # 소수면 리스트에 넣어주기

if len(num_list) == 0:
    print(-1)               # 리스트가 비었으면 -1 출력
else:
    print(sum(num_list))    # 합계 출력
    print(min(num_list))    # 최솟값 출력