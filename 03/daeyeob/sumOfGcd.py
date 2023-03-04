n = int(input())

def find_gcd(num1:int, num2:int) -> int:
    while (num2>0):
        num1,num2 = num2, num1%num2
    return num1

for _ in range(n):
    sumOfPairs = 0
    cdPairs = list(map(int,input().split()))
    quantity = cdPairs[0]
    for i in range(1,quantity):
        for j in range(i+1, quantity+1):
            sumOfPairs += find_gcd(cdPairs[i],cdPairs[j])
    print(sumOfPairs)