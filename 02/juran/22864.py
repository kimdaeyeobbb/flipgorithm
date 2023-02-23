A, B, C, M = map(int, input().split(' '))
nu = 0 #누적 피로도
work_h = 0 #일한 시간
rest_h = 0 #휴식 시간

if A > M:
  print(0)

else:
  while work_h + rest_h < 24:
    if nu < 0 : nu = 0
    if nu+A <= M:
      nu += A
      work_h += 1
    else:
      nu -= C
      rest_h += 1


  print(B * work_h)
