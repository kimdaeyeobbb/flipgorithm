
import random
n = int(input())
for i in range(n):
  r = random.randint(10,99)
  print(r, end = ' ')
  if r == 13:
    break
