#2015104124 진우빈

import utility
import sys

print("-------------------------- Matrix Chain Multiplication --------------------------\n\n")

d=[5,2,3,4,6,7,8]
n = len(d)

M = [[0 for j in range(n)] for i in range(n)]
P = [[0 for j in range(n)] for i in range(n)]

for diag in range(1, n):
    for i in range(1, n-diag):
        j = i+diag
        M[i][j] = sys.maxsize
        for k in range(i,j):
            if(M[i][j] > M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]):
                M[i][j] = M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]
                P[i][j] = k
    

def order(p,i,j):
    if(i==j):
        print("A",i,sep='', end='')
    else:
        k = p[i][j]
        print("(", end='')
        order(p,i,k)
        order(p,k+1,j)
        print(")", end='')
            

            
utility.printMatrix(M)
print()
utility.printMatrix(P)
print()
order(P,1,6)
print("\n\n")
print("-------------------------- Optimal Search Tree --------------------------\n\n")

class Node:
    def __init__(self, data):
        self.l_child=None
        self.r_child=None
        self.data = data
        
def tree(key, r, i, j):
    k = r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child=tree(key,r,i,k-1)
        p.r_child=tree(key,r,k+1,j)
        return p

key = [" ", "A", "B", "C", "D"]
p=[0, 0.375, 0.375, 0.125, 0.125]
n=len(p)-1

A=[[0 for j in range(0,n+2)] for i in range(0, n+2)]
R=[[0 for j in range(0,n+2)] for i in range(0, n+2)]

for i in range(1,n+1):
    A[i][i-1]=0
    A[i][i] = p[i]
    R[i][i] = i
    R[i][i-1] = 0
    
A[n+1][n] = 0
R[n+1][n] = 0

for diag in range(1, n):
    for i in range(1, n-diag+1):
        j = i+diag
        A[i][j] = sys.maxsize
        for k in range(i,j+1):
            if A[i][j] > A[i][k-1] + A[k+1][j]:
                A[i][j] = A[i][k-1] + A[k+1][j]
                R[i][j] = k
        
        for s in range(i,j+1):
            A[i][j] += p[s]

utility.printMatrixF(A)
print()
utility.printMatrix(R)
print()

root = tree(key,R,1,n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)
