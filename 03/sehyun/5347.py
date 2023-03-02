def gcd(a, b):
    while a:
        if a < b:
            a, b = b, a
        a = a % b
    return b

def lcm(a, b):
    L = int((a * b) / gcd(a, b))
    print(L)
    
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    lcm(a, b)