
import csv
from pathlib import Path
from collections import Counter

# Input and output file paths
project_dir = Path(__file__).resolve().parent.parent

input_file = (
    project_dir
    / "03_Genome_Annotation"
    / "Prokka_Output_Final"
    / "B_subtilis_168.tsv"
)
output_dir = Path(__file__).resolve().parent
summary_file = output_dir / "functional_annotation_summary.txt"
product_file = output_dir / "product_distribution.csv"

# Read Prokka annotation table
with open(input_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")
    records = list(reader)

# Select protein-coding sequences
cds_records = [
    record for record in records
    if record["ftype"].strip() == "CDS"
]

total_cds = len(cds_records)

# Identify hypothetical proteins
hypothetical = [
    record for record in cds_records
    if "hypothetical protein" in record["product"].lower()
]

# Identify uncharacterized proteins separately
uncharacterized = [
    record for record in cds_records
    if "uncharacterized protein" in record["product"].lower()
]

# Remaining CDS are assigned another product description
annotated = [
    record for record in cds_records
    if record not in hypothetical
    and record not in uncharacterized
    and record["product"].strip()
]
# Count gene, COG and EC annotations
gene_count = sum(
    bool(record["gene"].strip()) for record in cds_records
)

cog_count = sum(
    bool(record["COG"].strip()) for record in cds_records
)

ec_count = sum(
    bool(record["EC_number"].strip()) for record in cds_records
)

# Calculate percentages
hypothetical_percentage = (
    len(hypothetical) / total_cds * 100 if total_cds else 0
)

annotated_percentage = (
    len(annotated) / total_cds * 100 if total_cds else 0
)

# Count predicted product descriptions
product_counts = Counter(
    record["product"].strip()
    for record in cds_records
    if record["product"].strip()
)

# Save functional annotation summary
with open(summary_file, "w", encoding="utf-8") as file:
    file.write("FUNCTIONAL ANNOTATION ANALYSIS\n")
    file.write("Organism: Bacillus subtilis strain 168\n\n")

    file.write(f"Total CDS: {total_cds}\n")
    file.write(f"Functionally described CDS: {len(annotated)}\n")
    file.write(f"Hypothetical proteins: {len(hypothetical)}\n")
    file.write(f"Uncharacterized proteins: {len(uncharacterized)}\n")

    file.write(
        f"Functionally described CDS percentage: "
        f"{annotated_percentage:.2f}%\n"
    )

    file.write(
        f"Hypothetical protein percentage: "
        f"{hypothetical_percentage:.2f}%\n"
    )

    file.write(f"CDS with gene names: {gene_count}\n")
    file.write(f"CDS with COG assignments: {cog_count}\n")
    file.write(f"CDS with EC numbers: {ec_count}\n")

# Save product distribution
with open(product_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Number_of_CDS"])

    for product, count in product_counts.most_common():
        writer.writerow([product, count])

# Display results
print("FUNCTIONAL ANNOTATION ANALYSIS")
print("--------------------------------")
print("Total CDS:", total_cds)
print("Functionally described CDS:", len(annotated))
print("Hypothetical proteins:", len(hypothetical))
print("Uncharacterized proteins:", len(uncharacterized))
print(f"Functionally described CDS: {annotated_percentage:.2f}%")
print(f"Hypothetical proteins: {hypothetical_percentage:.2f}%")
print("CDS with gene names:", gene_count)
print("CDS with COG assignments:", cog_count)
print("CDS with EC numbers:", ec_count)

print("\nAnalysis completed successfully.")
print("Results saved in:", output_dir.resolve())
