n = input()
nn = n
i = 0
while True:
  if len(nn) == 1:
    nn = '0'+nn
  a = str(int(nn[0]) + int(nn[-1]))
  new = str(int(nn[-1] + a[-1]))
  nn = new
  i += 1
  if n == new:
    break
print(i)
