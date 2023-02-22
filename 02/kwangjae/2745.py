import sys 
from string import ascii_uppercase

letters={}
for i,letter in enumerate(ascii_uppercase):
    letters[letter]= i+10 
for i, num in enumerate([i for i in range(0,10)]):
    letters[str(num)]=i 
nums , notation = sys.stdin.readline().strip().split()
notation = int(notation)
answer= 0
for i,num in enumerate(nums[::-1]):
    answer+=(notation**i)*letters[num] 
    

print(answer)