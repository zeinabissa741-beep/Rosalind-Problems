k = 19 #AA
m = 27 #Aa
n = 29 #aa

total = k+m+n
    

#random mating = dominant allele:AA or Aa
#possible selection: km + kn + kk + mn*1/2 + mm*3/4

kk = k/total * (k-1)/(total-1)
km = 2*(k/total * m/(total-1))
kn = 2*(k/total * n/(total-1))
mm = 0.75*(m/total * (m-1)/(total-1))
mn = (m/total * n/(total-1))


proba = km + kn + kk + mn + mm
print(f"{proba:.5f}")


