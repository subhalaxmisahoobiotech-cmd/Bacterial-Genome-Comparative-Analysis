import matplotlib.pyplot as plt
from Bio import SeqIO

# Read genome sequence
file_path = "01_Genome_Sequences/B_subtilis_168_genome.fasta"
record = SeqIO.read(file_path, "fasta")
sequence = str(record.seq).upper()

# Nucleotide counts
bases = ["A", "T", "G", "C"]
counts = [sequence.count(base) for base in bases]

# GC and AT percentages
gc = ((counts[2] + counts[3]) / len(sequence)) * 100
at = ((counts[0] + counts[1]) / len(sequence)) * 100

# Create two graphs simultaneously
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Graph 1: Nucleotide composition
axes[0].bar(bases, counts)
axes[0].set_title("Nucleotide Composition")
axes[0].set_xlabel("Nucleotide Bases")
axes[0].set_ylabel("Number of Bases")

# Graph 2: GC and AT content
axes[1].pie(
    [gc, at],
    labels=["GC Content", "AT Content"],
    autopct="%1.2f%%",
    startangle=90
)
axes[1].set_title("GC and AT Content")

# Overall title
fig.suptitle("Bacillus subtilis 168 Genome Characterization")

plt.tight_layout()

# Save both graphs in one image
plt.savefig("B_subtilis_genome_analysis.png", dpi=300)

plt.show()