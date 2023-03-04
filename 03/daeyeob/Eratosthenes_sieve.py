n,k = map(int,input().split())
arr = [True for i in range(n+1)] # 2 ~ n. True -> 모든 수가 소수라 가정하고 시작. 합성수는 False 변환
num_count = 0

for num in range(2,n+1):  # 2 ~ n까지 확인
    for multiplier in range(num, n+1, num):  # num 의 배수 확인
        # print(multiplier)
        if (arr[multiplier]):  # arr[multiplier] == True (소수인 경우)
            num_count += 1 # 지우는 숫자 카운트 (소수 & 소수의 배수)
            arr[multiplier] = False # 지우고 난 다음 해당 숫자는 다시 False 처리 => 재카운팅 방지

            if (num_count == k):   # 카운팅한 횟수가 k번째 인 경우
                print(multiplier)   # 정답 출력