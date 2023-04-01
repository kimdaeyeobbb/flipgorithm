#백준2776 번 암기왕 문제
# 첫째 줄에 테스트케이스의 개수 T가 들어온다. 다음 줄에는 ‘수첩 1’에 적어 놓은 정수의 개수 N(1 ≤ N ≤ 1,000,000)이 입력으로 들어온다. 
# 그 다음 줄에  ‘수첩 1’에 적혀 있는 정수들이 N개 들어온다. 그 다음 줄에는 ‘수첩 2’에 적어 놓은 정수의 개수 M(1 ≤ M ≤ 1,000,000) 이 주어지고, 
# 다음 줄에 ‘수첩 2’에 적어 놓은 정수들이 입력으로 M개 들어온다. 
# 모든 정수들의 범위는 int 로 한다

from typing import Any, Sequence


def seq_search(a:Sequence, key:Any) -> int:
    
    i=0

    while True:
        if i == len(a):
            return 0
        if a[i] == key:
            return 1
        i += 1


if __name__ == '__main__':

    num1 = int(input())
    num2 = int(input())

    notebook1 = list(map(int, input().split()))
    notebook2 = list(map(int, input().split()))

    for i in range(len(notebook2)):
        ky = notebook2[i]
        idx=seq_search(notebook1, ky)

        if idx == 0:
            print("0")
        else:
            print("1")
            

