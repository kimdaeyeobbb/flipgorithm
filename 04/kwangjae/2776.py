import sys 
from collections import defaultdict
T = int(sys.stdin.readline().strip())

for i in range(T):
    N= sys.stdin.readline().strip()
    note1 = set(map(int,sys.stdin.readline().strip().split()))
    dict_note1=defaultdict(int)
    for i in note1:
       
        dict_note1[i]+=1
    M = N= sys.stdin.readline().strip()
    note2 = list(map(int,sys.stdin.readline().strip().split()))
    dict_note2=defaultdict(int)
    for i in note2:
        if dict_note1[i]==1:
            print(1)
        else: print(0)

