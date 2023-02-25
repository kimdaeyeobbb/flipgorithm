# 입력
N, B = input().split()

# B를 정수형으로 변환
B = int(B)

# N을 10진법으로 변환 후 출력
print(int(N, B))