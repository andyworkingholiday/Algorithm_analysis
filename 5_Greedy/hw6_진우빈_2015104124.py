import utility
import queue
e = {0 : [1, 2, 3], 1 : [2,5], 2 : [3, 4, 5, 6], 3 : [4,6], 4:[6, 7]}
N = 8
a = [[0 for j in range(0 , N)] for i in range(0, N)]
for i in range(0, N - 1):
    for j in range(i + 1, N):
        if i in e:
            if j in e[i]:
                a[i][j] = 1
                a[j][i] = 1
                
utility.printMatrix(a)
visited = N * [0]

def BFS(a, v):
    q = queue.Queue()
    visited[v] = 1
    q.put(v)
    while not q.empty():
        x = q.get()
        print(x)
        for i in range(N):
            if a[x][i] == 1 and visited[i] == 0:
                q.put(i)
                visited[i] = 1
                

                
                
BFS(a, 0)


def promissing(i, col):
    switch = True
    k = 0
    while k < i and switch:
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            switch = False
        k += 1
    
    return switch
    
    
    
def queens(n, i, col):
    if promissing(i, col):
        if i == n - 1:
            print(col)
            
        else:
            for j in range(n):
                col[i + 1] = j
                queens(n, i+1, col)
    
N = 7
col = N * [0]
queens(N, -1, col)
