def minmax(depth,index,maximizing_player,values,alpha,beta):
    if depth == 3:
        return values[index]
    
    if maximizing_player:
        best = float("-inf")
        for i in range(2):
            val = minmax(depth+1,index*2+i,False,values,alpha,beta)
            best = max(best,val)
        return best
    else:
        best = float("inf")
        for i in range(2):
            val = minmax(depth+1,index*2+i,True,values,alpha,beta)
            best = min(best,val)
        return best


values = [3, 5, 2, 9, 12, 5, 23, 23]

best = minmax(0,0,True,values,float("-inf"),float("inf"))
print("best : ",best)