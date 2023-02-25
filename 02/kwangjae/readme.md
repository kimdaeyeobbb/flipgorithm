문제1 

[https://www.acmicpc.net/problem/5618](https://www.acmicpc.net/problem/5618)

 [5618번: 공약수

첫째 줄에 n이 주어진다. n은 2 또는 3이다. 둘째 줄에는 공약수를 구해야 하는 자연수 n개가 주어진다. 모든 자연수는 108 이하이다.

www.acmicpc.net](https://www.acmicpc.net/problem/5618)

문제2 

[https://www.acmicpc.net/problem/2745](https://www.acmicpc.net/problem/2745)

 [2745번: 진법 변환

B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오. 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 

www.acmicpc.net](https://www.acmicpc.net/problem/2745)

문제3

[https://www.acmicpc.net/problem/22864](https://www.acmicpc.net/problem/22864)

 [22864번: 피로도

첫 번째 줄에 네 정수 $A$, $B$, $C$, $M$이 공백으로 구분되어 주어진다. 맨 처음 피로도는 0이다.

www.acmicpc.net](https://www.acmicpc.net/problem/22864)

문제4 

[https://www.acmicpc.net/problem/2609](https://www.acmicpc.net/problem/2609)

 [2609번: 최대공약수와 최소공배수

첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

www.acmicpc.net](https://www.acmicpc.net/problem/2609)

문제5

[https://www.acmicpc.net/problem/1934](https://www.acmicpc.net/problem/1934)

 [1934번: 최소공배수

두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있

www.acmicpc.net](https://www.acmicpc.net/problem/1934)

문제6

[https://www.acmicpc.net/problem/11653](https://www.acmicpc.net/problem/11653)

 [11653번: 소인수분해

첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

www.acmicpc.net](https://www.acmicpc.net/problem/11653)

문제7

[https://www.acmicpc.net/problem/1110](https://www.acmicpc.net/problem/1110)

 [1110번: 더하기 사이클

0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음,

www.acmicpc.net](https://www.acmicpc.net/problem/1110)

### **풀이**

---

**문제1**

```
import sys 
import math 
N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip(" ").split()))

def gcd(a,b): #math.gcd로 대체가능 
    for i in range(min(a,b),0, -1):
        if a % i == 0 and b % i == 0:
            return i 
if N==2: 
    gcd_ =gcd(nums[0], nums[1])
else: 
    gcd_ = gcd(gcd(nums[0], nums[1]), nums[2]) 
answer =set()
for i in range(1, int(gcd_**0.5)+1):
    if gcd_%i == 0:
        answer.add(i)
        answer.add(gcd_//i)
answer =sorted(answer)
print(*answer, sep="\n")
```

1.gcd 함수 정의 

2.주어진 숫자가 2개인 경우와 3개인 경우로 분리 

3.집합 자료형을 활용해 중복 소거 

4.범위는 root(gcd)

**문제2**

```
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
```

1.문자열->숫자에 대응하는 딕셔너리 생성 

2.n진법에 맞춰서 변환

**문제3**

```
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
```

경우1 피로도가 M보다 작거나 같은경우 

\-> 일 B증가 피로도 A증가 

경우2 피로도가 M보다 큰 경우 

\-> 일 -C

두 경우 모두 time+1

**문제4**

```
import sys 
from math import gcd
N = int(sys.stdin.readline().strip())
for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    print(a*b//gcd(a,b))
```

**문제5**

```
import sys 
from math import gcd
N = int(sys.stdin.readline().strip())
i = 2
while N!=1: 
    if N%i==0: 
        N=N//i
        print(i)
        i=2
    else: 
        i+=1
```

**문제6**

```
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
```