import sys 
from string import ascii_uppercase

A,B,C,M = map( int, sys.stdin.readline().strip().split() ) 
time = 0
tire= 0  
work =0 
while time!=24: 
    if tire+A<=M:
        work+=B
        tire+=A
        time+=1
    else: 
        tire-=C
        if tire<0: 
            tire = 0 
        time+=1
print(work)