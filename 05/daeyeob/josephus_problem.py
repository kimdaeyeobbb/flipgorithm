N,K= map(int,input().split())
A = []
Josephus_Permutation = []
index = 0

for i in range(N):
    A.append(i+1)

while len(A) > 0:
    index = (index + (K-1)) % len(A)

    Josephus_Permutation.append(A.pop(index))

print("<"+", ".join(map(str,Josephus_Permutation))+">")