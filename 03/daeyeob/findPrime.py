def isPrime(num:int) -> int:
    if (num < 2): return 0
    for i in range(2, int(num**0.5)+1):
        if (num % i == 0): return 0
    return 1

n = int(input())
numbers = list(map(int,input().split()))
numOfPrimes = 0
for num in numbers:
    numOfPrimes += isPrime(num)

print(numOfPrimes)