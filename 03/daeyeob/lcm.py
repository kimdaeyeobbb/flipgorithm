# 최대공약수 - 유클리드 호제법
# x,y의 최대공약수는 y와 x를y로 나눈 나머지값의 최대공약수와 동일하다
def gcd(num1, num2):
    while(num2>0):
        num1, num2 = num2, num1%num2
    return num1

# 최소공배수 - 두 수의 곱을 최대공약수로 나눈 몫
def lcm(num1, num2):
    return (num1*num2)//gcd(num1,num2)

n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    print(lcm(a,b))