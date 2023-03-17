n = int(input())

for i in range(n):
    ps = input()
    sum = 0
    for j in ps:
        if j == '(':
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            break
    if sum == 0:
        print("YES")
    else:
        print("NO")