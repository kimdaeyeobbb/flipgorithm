n = int(input())   # n 입력
num_list = list(map(int,input().split()))   # 입력된 자연수 리스트 생성

# 최대공약수 찾는 함수 정의
def find_gcd(a, b):
    while a:
        if a < b:
            a, b = b, a
        a = a % b
    return b

# 자연수 리스트에서 최대공약수 찾기
gcd = num_list[0]
for i in num_list:
    gcd = find_gcd(i, gcd)

# 최대공약수의 약수들 출력
for i in range(1, gcd+1):
    if gcd % i == 0:
        print(i)