
import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]

genomes = {
    "B. subtilis 168":
        project_dir / "03_Genome_Annotation/Prokka_Output_Final/B_subtilis_168.tsv",

    "B. licheniformis DSM13":
        project_dir / "03_Genome_Annotation/B_licheniformis_Prokka_Output/B_licheniformis_DSM13.tsv"
}

all_results = []

for organism, file_path in genomes.items():

    df = pd.read_csv(file_path, sep="\t", keep_default_na=False)

    cds = df[df["ftype"] == "CDS"].copy()

    enzyme_genes = cds[cds["EC_number"] != ""]

    print("\nOrganism:", organism)
    print("Total CDS:", len(cds))
    print("CDS with EC numbers:", len(enzyme_genes))
    print("Unique EC numbers:", enzyme_genes["EC_number"].nunique())

    for _, row in enzyme_genes.iterrows():
        all_results.append({
            "Organism": organism,
            "Locus_Tag": row["locus_tag"],
            "Gene": row["gene"],
            "EC_Number": row["EC_number"],
            "Product": row["product"]
        })

result_df = pd.DataFrame(all_results)

output_file = (
    project_dir / "04_Functional_Analysis/"
    "comparative_enzyme_assignments.csv"
)

result_df.to_csv(output_file, index=False)

print("\nComparative enzyme analysis completed.")
print("Results saved:", output_file)
