import math

DNA = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

#function to get the content out of a string
def GC_Content(dna):
    content = 0
    length = 0
    for c in dna:
        if c != '\n':
            length+=1
        if c =="G" or c=="C":
            content +=1
    percent = (content*100)/length
    return percent

#function to store the id and dna
def Read_File(fasta):
    i = 0
    id = ""
    dna = ""
    GC_id = ""
    GC_cont = 0
    for c in fasta:
        if c=="_": 
            start = i
            idNB = i+4
            while start< idNB:
                id+=fasta[start+1]
                start+=1
            start = idNB+2
            while start<len(fasta) :
                if fasta[start] != ">" :
                    dna+=fasta[start]
                else:
                    break
                start+=1

            if not math.isclose(GC_Content(dna), GC_cont, abs_tol = 0.001): 
                if GC_cont < GC_Content(dna): #accomodate absolute error here
                    GC_cont = GC_Content(dna)
                    GC_id = id
            
            id=""
            dna=""
        i+=1
    print(f"Rosalind_{GC_id} {GC_cont:.6f}%")

Read_File(DNA)  
