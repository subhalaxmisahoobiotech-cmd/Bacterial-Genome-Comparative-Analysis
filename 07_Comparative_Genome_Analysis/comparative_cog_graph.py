
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]

input_file = (
    project_dir / "04_Functional_Analysis/"
    "comparative_cog_category_counts.csv"
)

output_dir = project_dir / "05_Results_and_Graphs"

df = pd.read_csv(input_file)

# Create comparison table
comparison = df.pivot_table(
    index="COG_Category",
    columns="Organism",
    values="CDS_Count",
    aggfunc="sum",
    fill_value=0
)

comparison = comparison.sort_index()

# Generate grouped bar graph
comparison.plot(
    kind="bar",
    figsize=(14, 7),
    width=0.8
)

plt.title("Comparative COG Functional Category Distribution")
plt.xlabel("COG Functional Categories")
plt.ylabel("Number of CDS")
plt.xticks(rotation=0)
plt.legend(title="Organisms")
plt.tight_layout()

plt.savefig(
    output_dir / "Comparative_COG_Functional_Distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# Save comparison table
comparison.to_csv(
    project_dir / "04_Functional_Analysis/"
    "comparative_cog_comparison_table.csv"
)

print("Comparative COG graph generated successfully.")
print("Comparison table saved successfully.")
print(comparison)
