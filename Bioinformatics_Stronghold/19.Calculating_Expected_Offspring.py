data = "19902 16589 17514 19761 17280 17620"
genotypes = ["AA-AA", "AA-Aa", "AA-aa", "Aa-Aa", "Aa-aa", "aa-aa"]
dataset = [int(x) for x in data.split()]
dominant = 0

i = 0
while i < len(dataset):
    #getting the parent genotype
    if dataset[i] > 0:
        parent = genotypes[i]
        if parent in ["AA-AA", "AA-aa", "AA-Aa"]:
            dominant +=2 * dataset[i]
        elif parent == "Aa-Aa":
            dominant+=1.5 * dataset[i]
        elif parent == "Aa-aa":
                    dominant+=1 * dataset[i]
    i+=1
print(dominant)
