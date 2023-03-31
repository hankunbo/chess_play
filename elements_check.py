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
        elif set(elements[j]).issubset(list_2) :
            return 0
        elif len(imput) == 9:
            return 0.5
        