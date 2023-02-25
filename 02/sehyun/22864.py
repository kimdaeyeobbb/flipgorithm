# 1시간 일 할때
# A : 쌓인 피로도
# B : 처리한 일

# 1시간 쉴 떄
# C : 줄어든 피로도

# M : 최대 피로도

A, B, C, M = map(int, input().split())

time = 0
fatigue = 0
work = 0

while time < 24:
    if fatigue <= M-A:   # M을 넘지 않게 해주기 위해 M-A 이하일 때 일하는 것으로 설정
        fatigue += A
        work += B
        time += 1
    else:                # 피로도가 M-A 이상이면 쉬어주기
        fatigue -=  C
        time += 1
        if fatigue < 0:  # 피로도가 음수가 되면 0으로 변환
            fatigue = 0

print(work)
