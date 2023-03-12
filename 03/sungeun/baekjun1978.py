#백준 1978번 소수 개수 구하기

#주어진 주 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램 작성
#첫 줄에 수의 개의 N이 주어짐. N은 100 이하임. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수임
#주어진 수들 중 소수의 개수를 출력함

n=int(input())
data=list(map(int, input(). split()))
count=0
prime=[]

def is_prime(data):
    for i in range(2, data-1):
        if data % i == 0:
            return False
    return True

for i in range(1, len(data)):
    if(is_prime(data[i]) == True):
        prime.append(data[i])
        count += 1
    
      
print(prime)
print(count)
