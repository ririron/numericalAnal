def my_average(x):

    return sum(x) / len(x)

def my_median(x):

    if len(x) % 2 == 0:
        m = len(x) / 2
        return (x[int(m)-1] + x[int(m)]) / 2
    else :
        m = len(x) / 2 + 1
        return x[int(m)-1] 
    
    


test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
print(my_average(test))
print(my_median(test))
