def printMatrix(d):
    m = len(d)
    n = len(d[0])
    for i in range(0,m):
        for j in range(0,n):
            print("%4d" % d[i][j], end=" ")
        
        print()

#print float matrix

def printMatrixF(d):
    m = len(d)
    n = len(d[0])
    for i in range(0,m):
        for j in range(0,n):
            print("%5.2f" % d[i][j], end=" ")
    
        print()
