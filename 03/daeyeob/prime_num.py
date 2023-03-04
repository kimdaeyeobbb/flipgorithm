m = int(input())
n = int(input())
result = [-1]

def isPrime(n:int) -> int:
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if(n%i == 0): return 0
    return 1

for num in range(m,n+1):
    if isPrime(num):
        result.append(num)

if len(result) < 2:
    print(*result)
else:
    result.remove(-1)  # min 값이 -1이 아니게 만듦
    print(sum(result))
    print(min(result))