
elements = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
def check(imput):
    list_1=[]
    list_2=[]
    for i in range (len(imput)):
        if i%2==0:
            list_1.append(imput[i])
        else:
            list_2.append(imput[i]) 
    for j in range (len(elements)):
        if set(elements[j]).issubset(list_1) :
            return 1
        if set(elements[j]).issubset(list_2) :
            return 0
        
imput = [2,1,5,8,7,4,3] 
#print(check(imput))

#这个end是判断下一步能否赢 并输出步数
def end(x):
    x_total = [1,2,3,4,5,6,7,8,9]
    for item in x:
        x_total.remove(item)        
    a = len(x)%2
    #判断终点
    for item1 in x_total: 
        x0 = []
        for item in x:       
            x0.append(item)
        x0.append(item1)
        if check(x0) == 1-a:
            return item1
        
            
def end1(x):
    if check(x) == 1:
        return 1
    elif check(x) ==0:
        return -1
    elif len(x)==9:
        return 0




    
imput = [5]



import random

def maxmin_num(x):
    if len(x)==9:
        return x
    l =len(x)  
    def maxmin(x):
        
        x_total = [1,2,3,4,5,6,7,8,9]
        for item in x:
            x_total.remove(item)   
        if end1(x) != None:
            return end1(x)
        
        else:
            if len(x)%2==0:
                poss = []
                for item2 in x_total :
                    x1 = []                
                    for item in x:       
                        x1.append(item)
                    x1.append(item2)                
                    poss.append(maxmin(x1))
                if len(x1)-1 == l:               
                    return max(poss) , poss , x_total
                else:
                    return max(poss)
            else:
                poss0 = []
                for item3 in x_total :
                    x2 = []                
                    for item in x:       
                        x2.append(item)
                    x2.append(item3) 
                                   
                    poss0.append(maxmin(x2))
                                
                if len(x2)-1 == l:    
                    print(min(poss0) , poss0 , x_total)
                    return min(poss0) , poss0 , x_total
                else:
                    return min(poss0)
    maxmin_poss , poss , x_total  = maxmin(x)
    num = 0
    zu = []
    for item in poss:        
        if poss[num] == maxmin_poss:
            zu.append(num)
        num = num + 1
    random.shuffle(zu)
    x.append(x_total[zu[0]])
    return x

print(maxmin_num(imput))








