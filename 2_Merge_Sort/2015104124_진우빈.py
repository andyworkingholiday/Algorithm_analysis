#2015104124 전자공학과 진우빈

additional_space1 = 0 
additional_space2 = 0
flag = 1
flag2 = 0

# 첫 번째 합병정렬 구현

def merge1(h, m, U, V, S):
    i = j = k =0
    
    #비교하면서 합치기 
    while(i < h and j < m):
        if(U[i] < V[j]):
            S[k] = U[i]
            i+=1
        else:
            S[k] = V[j];
            j+=1
        k+=1
    
    # 추가하지 못한 부분 마저 추가하기 
    while(i < h):
        S[k] = U[i]
        k+=1
        i+=1
        
    while(j < h):
        S[k] = V[j]
        k+=1
        j+=1
        
def mergesort1(n, S):
    global additional_space1
    global flag
    if(n == 1):
        flag = 0
        return S
    h = n // 2
    m = n - h
    
    U = S[:h]
    V = S[h:]
    
    #추가로 사용한 공간 더해주기
    if(flag):
        additional_space1 += len(U)
        additional_space1 += len(V)
    
    mergesort1(h, U)
    mergesort1(m, V)
    return merge1(h, m, U, V, S)

# 두 번째 합병정렬 구현

def mergesort2(S):
    def sort(low, high):
        if high - low == 1:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        global flag2
        global additional_space2
        
        temp = []
        i, j = low, mid

        while i < mid and j < high:
            if S[i] < S[j]:
                temp.append(S[i])
                i += 1
            else:
                temp.append(S[j])
                j += 1

        while i < mid:
            temp.append(S[i])
            i += 1
        while j < high:
            temp.append(S[j])
            j += 1
        
        # 추가된 공간만큼 더해주기
        if(flag2 < len(temp)):
            additional_space2 += (len(temp) - flag2)
            flag2 = len(temp)
            
        for i in range(low, high):
            S[i] = temp[i - low]

    return sort(0, len(S))

# 임의의 S에 따른 결괏값 확인

s = [3,5,2,9,10,14,4,8]
print("After Merge1")
mergesort1(8,s)
print(s)
print("Additional Space : ",additional_space1,"\n")

s = [3,5,2,9,10,14,4,8]
print("After Merge2")
mergesort2(s)
print(s)
print("Additional Space : ",additional_space2,"\n")
