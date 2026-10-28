n = 82
m = 19

array=[0]*n
adults=[0]*n
offspring=[0]*n

array[0] = 1
array[1] = 1
adults[0] = 0
adults[1] = 1
offspring[0] = 1

i = 1
while i < len(array):
    offspring[i] = adults[i-1]
    if i >= m:
        adults[i] = offspring[i-1] + adults[i-1] - offspring[i-m]
    elif i>1:
        adults[i] = offspring[i-1] + adults[i-1]
    array[i] = adults[i] + offspring[i]
    i+=1

print(array[n-1])
