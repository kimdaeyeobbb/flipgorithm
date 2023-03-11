import sys 

N, M =map(int, sys.stdin.readline().strip().split(" "))
poke = {}
for i in range(1,N+1):
    i =str(i)
    name =sys.stdin.readline().strip()
    poke[i] =name
    poke[name] = i  
for j in range(M):
    ask = sys.stdin.readline().strip()
    print(poke[ask])