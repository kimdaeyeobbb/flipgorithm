#백준9613번 GCD합 구하기


import sys
import math
from itertools import permutations


n=int(input())                                   # 테스트 케이스의 개수 정하기기
#data=[]                                         # 데이터 입력될 리스트 변수 선언하기
gcdsum=0                                         # 최대공약수 합 변수 선언하기기

for i in range(n):
    data=list(map(int, input().split()))         # 데이터 입력 리스트
    gcdsum=0

    for j in range(n-1):                         #17-18 데이터 리스트에서 2개씩 데이터 순서쌍 추출 선언하기
        for k in range(j+1, n):
            gcdsum += math.gcd(data[j], data[k]) # 최대공약수 합 구하기기

    print(gcdsum)
