s = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

neu = open("rosalind.txt","r")
lines = neu.readlines()
a = 0

while a<len(s):
    codon = s[a]+s[a+1]+s[a+2]
    if codon in  ('UAA', 'UAG', 'UGA'):
        break
    else:
       for row in lines:
        if row.find(codon) != -1:
            line_list = row.split()
            codon_index = line_list.index(codon)
            amino = line_list[codon_index + 1]
            print(amino,end="")    
    a+=3

neu.close()