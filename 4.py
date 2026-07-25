def alpha_beta(depth,index,maximizingplayer,values,alpha,beta):
    if depth == 3:
        return values[index]

    if maximizingplayer:
        best = float("-inf")
        for i in range(2):
            val = alpha_beta(depth+1,index*2+i,False,values,alpha,beta)
            best = max(val,best)
            alpha = max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best = float("inf")
        for i in range(2):
            val = alpha_beta(depth+1,index*2+i,True,values,alpha,beta)
            best = min(best,val)
            beta = min(beta,best)
            if beta<=alpha:
                break
        return best
    
values = [3, 5, 2, 9, 12, 5, 23, 23]

# Start the Alpha-Beta Pruning algorithm
result = alpha_beta(0, 0, True, values, float('-inf'), float('inf'))
print("The optimal value is:", result)