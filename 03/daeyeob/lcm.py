# 최대공약수 - 유클리드 호제법
# x,y의 최대공약수는 y와 x를y로 나눈 나머지값의 최대공약수와 동일하다
# 나머지 값이 0일떄의 y값이 최대공약수임 (마지막에 y를 x자리에 집어넣으므로 x를 출력하는 것)
# 참고자료: https://codingpractices.tistory.com/34
def gcd(num1, num2):
    while(num2>0):
        num1, num2 = num2, num1%num2
    return num1

# 최소공배수 - 두 수의 곱을 최대공약수로 나눈 몫
# 원래 최소공배수는 두 수의 공약수와 각각이 가지는 숫자들의 곱임
def lcm(num1, num2):
    return (num1*num2)//gcd(num1,num2)

n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    print(lcm(a,b))