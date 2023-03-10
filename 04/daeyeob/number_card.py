n = int(input())   # 상근이가 가지고 있는 숫자 카드의 개수
num_of_card = list(map(int,input().split()))   # 숫자 카드에 적힌 정수

m = int(input())  # 상근이 카드 판별 정수 개수
has_card = list(map(int,input().split()))  # 상근이가 가지고 있는 카드인지 아닌지 구해야할 정수

num_of_card.sort()

for num in has_card:  # num: 찾고자 하는 값 (존재 유무 파악해야하는 숫자)
    start, end = 0, len(num_of_card) - 1
    result = 0
    while(start <= end):
        mid = (start+end)//2
        if(num_of_card[mid] > num):
            end = mid-1
        elif (num_of_card[mid] < num):
            start = mid+1
        else:
            result = 1
            break
    print(result, end=' ')