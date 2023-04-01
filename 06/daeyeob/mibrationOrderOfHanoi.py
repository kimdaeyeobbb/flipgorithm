N = int(input())   # 원판 개수
result_list = []

def hanoi(n, source, dest, temp):   # source : 원반이 놓인 축, dest : 목적지, temp : 임시 축
    if (n == 1):
        result_list.append((source, dest))
    else:
        hanoi(n-1, source, temp, dest)   # 재귀 이용 (n에서 n-1로 변경)
        result_list.append((source,dest))
        hanoi(n-1, temp, dest, source)

hanoi(N,1,3,2)

print(len(result_list))
for i in range(len(result_list)):
    print(*(result_list[i]))