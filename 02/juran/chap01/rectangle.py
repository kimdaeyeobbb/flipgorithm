#my solution

area = int(input())

for i in range(1, int(area**(1/2)) +1):
  if area%i == 0:
    print(f'{i} x {area//i}')
    
    
#book's solution
area = int(input())
for i inr range(1, area+1):
  if i*i > area: break
  if area%i:continue
  print(f'{i} x {area//i}')
