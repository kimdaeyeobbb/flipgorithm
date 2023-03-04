#1
while True:
  n = int(input())
  if n >= 10 and n <= 99:
    break
print(n)

#2 비교 연산자를 연속으로 사용하는 경우
while True:
  n = int(input())
  if 10 <= n <= 99:
    break
print(n)

#3 드모르간의 법칙 사용
while True:
  n = int(input())
  if not(n<10 or n>99):
    break
print(n)
