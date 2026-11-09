
import subprocess
import os

# Genome file paths
query = "01_Genome_Sequences/B_subtilis_168_genome.fasta"

subject = (
    "01_Genome_Sequences/Comparison_Genome/"
    "B_licheniformis_DSM13_genome.fasta"
)

output_dir = "07_Comparative_Genome_Analysis"
os.makedirs(output_dir, exist_ok=True)

database_dir = os.path.join(output_dir, "BLAST_Database")
os.makedirs(database_dir, exist_ok=True)

database_prefix = os.path.join(
    database_dir, "B_licheniformis_DSM13"
)

# Create BLAST database
make_db = [
    "/opt/anaconda3/envs/prokka_env/bin/makeblastdb",
    "-in", subject,
    "-dbtype", "nucl",
    "-out", database_prefix
]

subprocess.run(make_db, check=True)

print("BLAST database created successfully.")

# Run BLASTn
blast_output = os.path.join(
    output_dir, "B_subtilis_vs_B_licheniformis_BLAST.tsv"
)

blast_command = [
    "/opt/anaconda3/envs/prokka_env/bin/blastn",
    "-query", query,
    "-db", database_prefix,
    "-out", blast_output,
    "-outfmt",
    "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore",
    "-evalue", "1e-10",
    "-num_threads", "2"
]

subprocess.run(blast_command, check=True)

print("BLASTn comparison completed successfully.")
print("Results saved:", blast_output)
