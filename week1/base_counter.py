dna = "ATGCGATTTAACCCGG"
counts = {"A":0,
         "T":0,
         "G":0,
         "C":0
         }
for base in dna:
    counts[base] +=1

    print(counts)