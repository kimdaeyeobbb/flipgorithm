import math
T = int(input())
ls = []
while T != 0:
    A, B = map(int, input().split())
    ls.append([A,B])
    T = T-1
for i in range(len(ls)):
  a = ls[i][0]
  b = ls[i][1]
  print(int((a*b/math.gcd(a,b)))
