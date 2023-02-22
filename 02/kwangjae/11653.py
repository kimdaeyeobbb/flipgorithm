import sys 
N = (sys.stdin.readline().strip())
cycle =0 
cycle_N = N 
while True: 
    if int(cycle_N)<10: 
        cycle_N ='0'+cycle_N[-1]
        cycle_N = cycle_N[-1]+str(int(cycle_N[0])+int(cycle_N[1]))[-1]
        cycle+=1 
        if int(cycle_N) == int(N):
            break 
    else:
        cycle_N = cycle_N[-1]+str(int(cycle_N[0])+int(cycle_N[1]))[-1]
        cycle+=1
      
        if int(cycle_N) == int(N):
            break 
print(cycle)