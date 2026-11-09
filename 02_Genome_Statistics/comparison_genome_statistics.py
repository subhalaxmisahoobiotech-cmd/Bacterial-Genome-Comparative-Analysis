
from Bio import SeqIO
from pathlib import Path

# Project directory
project_dir = Path(__file__).resolve().parent.parent

# Input genome
genome_file = (
    project_dir
    / "01_Genome_Sequences"
    / "Comparison_Genome"
    / "B_licheniformis_DSM13_genome.fasta"
)

# Read genome
record = SeqIO.read(genome_file, "fasta")
sequence = str(record.seq).upper()

# Genome statistics
genome_length = len(sequence)

A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")

GC_content = ((G + C) / genome_length) * 100
AT_content = ((A + T) / genome_length) * 100

# Display results
print("\nGENOME STATISTICS")
print("Organism: Bacillus licheniformis DSM 13")
print("Accession: CP000002.1")

print("\nGenome length:", genome_length, "bp")
print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)

print("GC content:", round(GC_content, 2), "%")
print("AT content:", round(AT_content, 2), "%")
