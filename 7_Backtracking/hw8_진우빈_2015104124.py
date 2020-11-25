#어려워서 그만 문제를 해결하지 못했습니다. 죄송합니다...
#2015104124 진우빈

import queue

class Node:
    def __init__(self, level, weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include
        
def kp_BFS():
    global maxProfit
    global bestset
    global w, W
    global p
    q = queue.Queue()
    
    u = Node(0,0,0,0)
    v = Node(0,0,0,0)
    q.put(v)
    while not q.empty():
        x = q.get()
        u.level = x.level + 1
        u.weight = x.weight + w[u.level - 1]
        u.profit = x.profit + p[u.level - 1]
        
        if u.weight <= W and u.profit > maxProfit:
            maxProfit = u.profit
        if compBound(u) > maxProfit:
            q.put(u)
            
        u.weight = x.weight
        u.profit = x.profit
        if compBound(u) > maxProfit:
            q.put(u)
            
def compBound(u):
    global W, w
    global N
    global p
    
    if u.weight >= W:
        return 0
    
    else:
        result = u.profit
        j = u.level + 1
        totalweight = u.weight
        while j < N and totalweight + w[j] <= W:
            totalweight += w[j]
            result += p[j]
            j += 1
            
        k = j
        if k < N:
            result += (W - totalweight) * p[k] / w[k]
            
        return result
        
        

        
N = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
include = [0] * N
maxProfit = 0
bestset = [0] * N
kp_BFS()
print(bestset)
