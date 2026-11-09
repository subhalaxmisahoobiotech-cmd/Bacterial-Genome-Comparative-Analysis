
import pandas as pd
from pathlib import Path
from collections import Counter

project_dir = Path(__file__).resolve().parents[1]

genomes = {
    "B. subtilis 168":
        project_dir / "03_Genome_Annotation/Prokka_Output_Final/B_subtilis_168.tsv",

    "B. licheniformis DSM13":
        project_dir / "03_Genome_Annotation/B_licheniformis_Prokka_Output/B_licheniformis_DSM13.tsv"
}

reference_file = (
    project_dir / "04_Functional_Analysis/COG_Reference/cog-24.def.tab"
)

# Load COG functional category reference
cog_reference = {}

with open(reference_file, encoding="utf-8") as file:
    for line in file:
        fields = line.rstrip("\n").split("\t")
        if len(fields) >= 2:
            cog_reference[fields[0]] = fields[1]

all_results = []

for organism, file_path in genomes.items():

    df = pd.read_csv(file_path, sep="\t", keep_default_na=False)
    cds = df[df["ftype"] == "CDS"]

    category_counts = Counter()

    for cog in cds["COG"]:
        if cog in cog_reference:
            categories = cog_reference[cog]

            for category in categories:
                if category.isalpha() and category.isupper():
                    category_counts[category] += 1

    for category, count in category_counts.items():
        all_results.append({
            "Organism": organism,
            "COG_Category": category,
            "CDS_Count": count
        })

result_df = pd.DataFrame(all_results)

output_file = (
    project_dir / "04_Functional_Analysis/"
    "comparative_cog_category_counts.csv"
)

result_df.to_csv(output_file, index=False)

print("COMPARATIVE COG ANALYSIS")
print("------------------------")
print(result_df.to_string(index=False))
print("\nResults saved:", output_file)
