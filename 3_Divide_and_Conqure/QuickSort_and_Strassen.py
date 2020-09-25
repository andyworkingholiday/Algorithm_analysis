#2015104124 진우빈
#HW3

#QuickSort

def quicksort(S, low, high):
    if high <= low:
        return
    pivot = partition(S, low, high)
    quicksort(S, low, pivot -1)
    quicksort(S, pivot + 1, high)
    
def partition(S, low, high):
    pivot = S[low]
    j = low
    for i in range(low+1, high+1):
        if S[i] < pivot:
            j+=1
            S[i], S[j] = S[j], S[i]
    
    #pivot point 설정안하고 j값 return하면 그게 pivot point
    S[low], S[j] = S[j], S[low]
    return j

s = [3,5,2,9,10,14,4,8]
quicksort(s, 0, 7)
print(s)
print("\n---------------------------\n")


#Strassen 행렬 곱

import numpy as np
threshold = 2

def strassen(n, A, B, C):
    if n <= threshold:
        C = np.array(A) @ np.array(B)
        return C
    
    A11 = np.array([[A[rows][cols] for cols in range(n//2)] for rows in range(n//2)])
    A12 = np.array([[A[rows][cols] for cols in range(n//2, n)] for rows in range(n//2)])
    A21 = np.array([[A[rows][cols] for cols in range(n//2)] for rows in range(n//2, n)])
    A22 = np.array([[A[rows][cols] for cols in range(n//2, n)] for rows in range(n//2, n)])
    
    B11 = np.array([[B[rows][cols] for cols in range(n//2)] for rows in range(n//2)])
    B12 = np.array([[B[rows][cols] for cols in range(n//2, n)] for rows in range(n//2)])
    B21 = np.array([[B[rows][cols] for cols in range(n//2)] for rows in range(n//2, n)])
    B22 = np.array([[B[rows][cols] for cols in range(n//2, n)] for rows in range(n//2, n)])
    
    M1 = M2 = M3 = M4 = M5 = M6 = M7 = np.array([])
    
    M1 = strassen(int(n/2), (A11 + A22), (B11 + B22), M1)
    M2 = strassen(int(n/2), (A21 + A22), B11, M2)
    M3 = strassen(int(n/2), A11, (B12 - B22), M3)
    M4 = strassen(int(n/2), A22, (B21 - B11), M4)
    M5 = strassen(int(n/2), (A11 + A12), B22, M5)
    M6 = strassen(int(n/2), (A21 - A11), (B11 + B12), M6)
    M7 = strassen(int(n/2), (A12 - A22), (B21 + B22), M7)
    
    C = np.vstack([np.hstack([M1+M4-M5+M7, M3+M5]), np.hstack([M2+M4, M1+M3-M2+M6])])
    return C
    
N = 4
A = [[1,2,0,2], [3,1,0,0], [0,1,1,2], [2,0,2,0]]
B = [[0,3,0,2], [1,1,4,0], [1,1,0,2], [0,5,2,0]]

Simple_Matrix = np.array(A) @ np.array(B)
Strassen_Matrix = [[0 for cols in range(N)] for rows in range(N)]

Strassen_Matrix = strassen(N, A, B, Strassen_Matrix)

print("Simple_Matrix\n", Simple_Matrix,"\n")
print("Strassen_Matrix\n",Strassen_Matrix,"\n")

flag = 1
for i in range(N):
    for j in range(N):
        if Simple_Matrix[i][j] != Strassen_Matrix[i][j]:
            flag = 0
            break
            
if flag: 
    print("It's Same!")
else:
    print("It's Not Same!")
