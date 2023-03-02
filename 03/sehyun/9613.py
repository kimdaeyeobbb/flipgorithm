# 9613번 GCD 합

t = int(input())

def gcd(a, b):   # 최대공약수 gcd 만드는 함수
    while a:
        if a < b:
            a, b = b, a
        a = a % b
    return b

for _ in range(t):
    sum = 0  # 테스트 케이스마다 sum 초기화
    num_list = list(map(int, input().split())) # 테스트 케이스를 한 줄로 받아 리스트로 만들기
    n = num_list.pop(0)  # 리스트 맨 앞 요소를 n을 따로 빼서 저장
    for i in range(n-1): # 리스트에서 마지막 인덱스를 뺀 모든 요소에 대해 반복
        for j in range(i+1, n):  # 리스트에서 첫번째 인덱스를 뺀 모든 요소에 대해 반복
            sum += gcd(num_list[i], num_list[j])
    print(sum)