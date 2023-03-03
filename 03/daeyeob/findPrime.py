def isPrime(num):
    if (num < 2): return False
    for i in range(2, num):
        if (num % i == 0): return False
    return True

n = int(input())
numbers = list(map(int,input().split()))
numOfPrimes = 0
for num in numbers:
    if(isPrime(num)): numOfPrimes += 1

print(numOfPrimes)