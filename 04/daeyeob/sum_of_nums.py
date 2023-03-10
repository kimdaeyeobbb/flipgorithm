s = int(input())
n = 1
while(s >= (n*(n+1))/2):  # 등차수열의 합 : (n*(n+1))/2
    n += 1

print(n-1)  # while문을 빠져나갔다는것은 등차합이 s보다 커졌다는 것이므로 n에서 1개 빼줘야함