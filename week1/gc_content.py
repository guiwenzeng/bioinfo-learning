# GC content: 
# (G count + C count) / Total length x 100
# Higher GC content can affect: DNA stability & Sequencing difficulty

def gc_content(sequence):

    g = sequence.count("G")
    c = sequence.count("C")

    gc = g + c

    percentage = gc / len(sequence) * 100

    return percentage

dna = "ATGCGCGAT"
gc_content(dna)