
import pandas as pd
from pathlib import Path

# Project directory
project_dir = Path(__file__).resolve().parents[1]

# Prokka annotation files
genomes = {
    "Bacillus subtilis 168":
        project_dir / "03_Genome_Annotation/Prokka_Output_Final/B_subtilis_168.tsv",

    "Bacillus licheniformis DSM13":
        project_dir / "03_Genome_Annotation/B_licheniformis_Prokka_Output/B_licheniformis_DSM13.tsv"
}

results = []

for organism, file_path in genomes.items():

    df = pd.read_csv(file_path, sep="\t", keep_default_na=False)

    # Consider CDS features only
    cds = df[df["ftype"] == "CDS"].copy()

    total_cds = len(cds)

    hypothetical = cds["product"].str.contains(
        "hypothetical protein", case=False
    ).sum()

    uncharacterized = cds["product"].str.contains(
        "uncharacterized protein", case=False
    ).sum()

    described = total_cds - hypothetical - uncharacterized

    gene_assigned = (cds["gene"] != "").sum()
    cog_assigned = (cds["COG"] != "").sum()
    ec_assigned = (cds["EC_number"] != "").sum()

    results.append({
        "Organism": organism,
        "Total CDS": total_cds,
        "Described CDS": described,
        "Hypothetical proteins": hypothetical,
        "Uncharacterized proteins": uncharacterized,
        "Gene assignments": gene_assigned,
        "COG assignments": cog_assigned,
        "EC assignments": ec_assigned
    })

    print("\nOrganism:", organism)
    print("Total CDS:", total_cds)
    print("Described CDS:", described)
    print("Hypothetical proteins:", hypothetical)
    print("Uncharacterized proteins:", uncharacterized)
    print("Gene assignments:", gene_assigned)
    print("COG assignments:", cog_assigned)
    print("EC assignments:", ec_assigned)

# Save comparison
output = pd.DataFrame(results)

output_path = (
    project_dir / "04_Functional_Analysis/"
    "comparative_functional_annotation.csv"
)

output.to_csv(output_path, index=False)

print("\nComparative functional annotation completed.")
print("Results saved:", output_path)
