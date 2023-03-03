import sys 

N,M = map(int,sys.stdin.readline().strip().split())

A= []
A_zeros=[]
for i in range(N):
    A_i= list(map(int, sys.stdin.readline().strip().split()))
    A.append(A_i)
    A_zeros = [0 for i in range(len(A_i))]

def dot(a:list,b:list):
    c =[[] for i in range(N)]
    for i in range(N):
        for j in range(N):
            c_ij = 0 
            for k in range(N):
                c_ij+=a[i][k]*b[k][j]
            c[i].append(c_ij%1000)
    return c

A_sum =None 
for degit in (bin(M)[2:][::-1]):
    if degit!="0" and A_sum==None:
        A_sum =A
    elif degit !="0" and A_sum!=None:
        A_sum=dot(A_sum,A)

    A =dot(A,A)
for i in range(len(A_sum)):
    for j in range(len(A_sum)):
        if A_sum[i][j]==1000:
            A_sum[i][j]=0
for row in A_sum: 
    print(*row, sep=" ")