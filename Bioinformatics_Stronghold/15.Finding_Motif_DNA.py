s = "GATATATGCATATACTT"
t = "CACAAACCA"

j = 0
index = len(s)-len(t) #13

while j<len(s): #j=1
    if s[j:j+len(t)] == t: 
        index=j #index=1
        print(index+1, end=" ")
    else:
        index = len(s)-len(t) #13
    j+=1 

    