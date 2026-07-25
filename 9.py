def objective_fun(x):
    return -(x**2)+10*x

def hill_climbing(start,step_size,max_i):
    current = start
    current_val = objective_fun(start)

    for i in range(max_i):
        left = current-step_size
        right = current+step_size

        left_val = objective_fun(left)
        right_val = objective_fun(right)

        if left_val > current_val:
            current_val = left_val
            current = left
        elif right_val > current_val:
            current_val = right_val
            current = right
        else:
            break
    return current,current_val

c,cv = hill_climbing(0.1,0.05,5)

print("current : ",c,"\ncurrent_val : ",cv)