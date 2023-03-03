# 2960번 에라토스테네스의 체

N, K = map(int, input().split())

num_list = [i for i in range(2, N+1)]


while K != 0:
    P = min(num_list)
    i = P
    num_list.remove(P)
    K -= 1
    if K == 0:   # 이 if문이 없으면 K가 0인데도 불구하고 아래 for문을 시작하게 됨
        break
    for i in num_list:
        if i % P == 0:
            num_list.remove(i)
            K -= 1
        if K == 0:  # 이 if문이 없으면 K가 음수로 내려가도 계속 for문이 돌아감
            break

print(i)