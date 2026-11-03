from Bio import SeqIO
from pathlib import Path

fasta_file = Path(__file__).parent / "rosalind.fasta"
code = []
seq = []
k = 3

for record in SeqIO.parse(fasta_file, "fasta"):
    code.append(record.id)
    seq.append(str(record.seq))

def overlap(a,b,k):
     if a[-k:] == b[:k]:
        return k
     return 0

def addEdge(adj,u,v):
    adj[u].append(v)

def displayAdjList(adj):
    for i in range(len(adj)):
        for j in adj[i]:
            print(code[i], code[j])

adj = [[] for _ in range(len(code))]

for i, a in enumerate(seq):
    for j, b in enumerate(seq):
        if i!=j:
            if overlap(a,b,k) == k:
                addEdge(adj, i, j)

displayAdjList(adj)