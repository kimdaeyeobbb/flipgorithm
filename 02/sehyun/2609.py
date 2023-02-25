# 2609번 최대공약수와 최소공배수

def gcd(a, b):
    while a:
        if a < b:
            a, b = b, a
        a = a % b
    return b

a, b = map(int, input().split())

G = gcd(a, b)
L = int((a * b) / G)

print(G, L, sep="\n")