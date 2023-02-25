import math
n = int(input())
if n == 2:
  a, b = map(int, input().split())
  gcd = math.gcd(a,b)

elif n == 3:
  a,b,c = map(int, input().split())
  gcd1 = math.gcd(a,b)
  gcd = math.gcd(gcd1, c)

gcd2 = []
for i in range(1,int(gcd**(1/2))+1):
  if gcd%i == 0:
    gcd2.append(i)
    if (i != (gcd//i)):
      gcd2.append(gcd//i)
gcd2.sort()
for i in gcd2:
  print(i, end='\n')
