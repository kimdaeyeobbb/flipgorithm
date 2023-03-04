# 4134번 다음 소수

t = int(input())

def prime(n):
    if n == 0:
        print(2)
    else:
        while True:
            for i in range(2, int(n**(1/2))+1):
                if n % i == 0:
                    n += 1
                    break
            else:
                print(n)
                break

for _ in range(t):
    n = int(input())
    prime(n)