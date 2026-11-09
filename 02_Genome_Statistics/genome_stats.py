from Bio import SeqIO
file_path = "01_Genome_Sequences/B_subtilis_168_genome.fasta"
record = SeqIO.read(file_path, "fasta")
sequence = str(record.seq).upper()

# Calculate genome length
genome_length = len(sequence)

# Calculate nucleotide composition
A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")

# Calculate GC and AT content
gc_content = ((G + C) / genome_length) * 100
at_content = ((A + T) / genome_length) * 100

# Display results
print("\nBACTERIAL GENOME CHARACTERIZATION")
print("-----------------------------------")
print("Organism: Bacillus subtilis 168")
print("Genome length:", genome_length, "bp")
print("Adenine (A):", A)
print("Thymine (T):", T)
print("Guanine (G):", G)
print("Cytosine (C):", C)
print("GC content:", round(gc_content, 2), "%")
print("AT content:", round(at_content, 2), "%")