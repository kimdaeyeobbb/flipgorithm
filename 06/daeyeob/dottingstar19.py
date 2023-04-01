def dottingStar(n,x,y):

    length = 1 + (n - 1) * 4

    if (n==1): grid[y][x]="*"; return;

    for i in range(length):
        grid[y][x+i] = '*'
        grid[y+i][x] = '*'
        grid[y+length-1][x+i] = '*'
        grid[y+i][x+length-1] = '*'

    dottingStar(n-1,x+2,y+2)

if __name__=="__main__":    # 메인함수의 선언 및 시작
    n = int(input())
    initlength = 1 + (n-1)*4
    grid = [[' ']*(initlength) for _ in range(initlength)]

    dottingStar(n,0,0)

    for star in grid: print(''.join(star))