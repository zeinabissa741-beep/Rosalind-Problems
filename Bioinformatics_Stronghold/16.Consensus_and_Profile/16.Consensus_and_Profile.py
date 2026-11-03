list = []
current_seq = []

#reading file
with open("rosalind.txt", "r") as file:
  for line in file:
    line = line.strip()
    if not line:
      continue
    if line.startswith(">"):
      if current_seq:
        list.append("".join(current_seq))
        current_seq = []
    else:
      current_seq.append(line)
  if current_seq:
    list.append("".join(current_seq))

DNA_length = len(list[0])
print(len(list))
print(DNA_length)

#creating matrix
rows = 4
cols = DNA_length
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

#filling the matrix with nucleotide occurence
i=0
j=0
while i<DNA_length:
    j=0
    while j<len(list):
        neu = list[j][i]
        if neu == "A":
            matrix[0][i]+=1
        if neu == "C":
            matrix[1][i]+=1
        if neu == "G":
            matrix[2][i]+=1
        if neu == "T":
            matrix[3][i]+=1
        j+=1
    i+=1

#printing the average DNA:
max = 0
counter=0
i=0
while i<DNA_length:
    counter=0
    max=0
    while counter<4:
        if matrix[counter][i] > max:
            max = matrix[counter][i]
            max_index=counter
        counter+=1
    if max_index==0:
        print("A",end="")
    if max_index==1:
        print("C",end="")
    if max_index==2:
        print("G",end="")
    if max_index==3:
        print("T",end="")
    i+=1
    
i=0
#printing matrix
listN = ["\nA","C","G","T"]
for row in matrix:
    print(f"{listN[i]}: ", end="")
    print(*row)
    i+=1

