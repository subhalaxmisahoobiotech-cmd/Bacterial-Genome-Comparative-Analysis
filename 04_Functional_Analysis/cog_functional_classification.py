
import csv
from pathlib import Path
from collections import Counter

# Define project paths
project_dir = Path(__file__).resolve().parent.parent

prokka_file = (
    project_dir
    / "03_Genome_Annotation"
    / "Prokka_Output_Final"
    / "B_subtilis_168.tsv"
)

cog_definition_file = (
    project_dir
    / "04_Functional_Analysis"
    / "COG_Reference"
    / "cog-24.def.tab"
)

cog_function_file = (
    project_dir
    / "04_Functional_Analysis"
    / "COG_Reference"
    / "cog-24.fun.tab"
)

output_dir = Path(__file__).resolve().parent


# Step 1: Read COG functional category descriptions
category_names = {}

with open(cog_function_file, "r", encoding="utf-8") as file:
    for line in file:
        fields = line.rstrip("\n").split("\t")

        if len(fields) == 4:
            category_code = fields[0]
            category_name = fields[3]
            category_names[category_code] = category_name


# Step 2: Read COG definitions
cog_definitions = {}

with open(cog_definition_file, "r", encoding="utf-8") as file:
    for line in file:
        fields = line.rstrip("\n").split("\t")

        if len(fields) >= 3:
            cog_id = fields[0]
            category_code = fields[1]
            cog_name = fields[2]

            cog_definitions[cog_id] = (category_code, cog_name)


# Step 3: Read Prokka annotations
category_counts = Counter()
matched_cds = 0
unmatched_cogs = set()
total_cds_with_cog = 0

with open(prokka_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")

    for row in reader:
        if row["ftype"] != "CDS":
            continue

        cog_id = row["COG"].strip()

        if not cog_id:
            continue

        total_cds_with_cog += 1

        if cog_id in cog_definitions:
            category_code, cog_name = cog_definitions[cog_id]
            matched_cds += 1

            for code in category_code:
                if code in category_names:
                    category_counts[code] += 1
        else:
            unmatched_cogs.add(cog_id)


# Step 4: Display results
print("\nCOG FUNCTIONAL CLASSIFICATION")
print("Organism: Bacillus subtilis strain 168")

print("\nTotal CDS with COG assignments:", total_cds_with_cog)
print("CDS matched with COG2024:", matched_cds)
print("Unmatched COG IDs:", len(unmatched_cogs))

print("\nFUNCTIONAL CATEGORY DISTRIBUTION")

for code, count in sorted(category_counts.items()):
    name = category_names[code]
    percentage = (count / matched_cds) * 100 if matched_cds else 0

    print(f"{code} - {name}: {count} CDS ({percentage:.2f}%)")


# Step 5: Save results
output_file = output_dir / "COG_functional_classification.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Category_Code",
        "Functional_Category",
        "Number_of_CDS",
        "Percentage"
    ])

    for code, count in sorted(category_counts.items()):
        percentage = (count / matched_cds) * 100 if matched_cds else 0

        writer.writerow([
            code,
            category_names[code],
            count,
            round(percentage, 2)
        ])

print("\nResults saved to:", output_file)
