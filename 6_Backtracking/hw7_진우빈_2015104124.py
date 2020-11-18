#2015104124 진우빈

#과제 1
N = 4
w = [1, 4, 2, 6]
W = 6
include = N * [0]
total = 0

def promissing(i, weight, total):
    global W, w, include
    return (weight + total >= W) and (weight == W or weight + w[i + 1] <= W)

def s_s(i, weight, total):
    global W, w, include
    if promissing(i, weight, total):
        if weight == W:
            print("sol", include)
        else:
            include[i + 1] = 1
            s_s(i + 1, weight + w[i + 1], total - w[i + 1])
            include[i + 1] = 0
            s_s(i + 1, weight, total - w[i + 1])

print("#1 --------------------")
print("items = ", w, "W = ", W)
for k in w:
    total += k
  
s_s(-1, 0, total)
print('\n')

#과제 2
N = 4
W = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
vcolor = N * [0]
M = 3
def m_coloring(i):
    global vcolor, N, M
    
    if promissing(i):
        if i == N - 1:
            print(vcolor)
        else:
            for color in range(M):
                vcolor[i + 1] = color + 1
                m_coloring(i + 1)
    
def promissing(i):
    global vcolor, W
    flag = True
    j = 0
    while j < i and flag:
        if W[i][j] and vcolor[i] == vcolor[j]:
            flag = False
        j += 1
        
    return flag
    
print("#2 --------------------")
m_coloring(-1)
