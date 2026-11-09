
import csv
from pathlib import Path
import matplotlib.pyplot as plt

# Project directories
project_dir = Path(__file__).resolve().parent.parent

input_file = (
    project_dir
    / "04_Functional_Analysis"
    / "COG_functional_classification.csv"
)

output_dir = project_dir / "05_Results_and_Graphs"
output_dir.mkdir(exist_ok=True)

# Read COG classification results
categories = []
counts = []

with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        categories.append(
            row["Category_Code"] + " - " + row["Functional_Category"]
        )
        counts.append(int(row["Number_of_CDS"]))

# Sort categories by number of CDS
sorted_data = sorted(
    zip(counts, categories)
)

counts = [item[0] for item in sorted_data]
categories = [item[1] for item in sorted_data]

# Generate horizontal bar graph
plt.figure(figsize=(12, 10))

bars = plt.barh(categories, counts)

plt.xlabel("Number of CDS")
plt.ylabel("COG Functional Categories")
plt.title(
    "COG Functional Category Distribution in Bacillus subtilis 168"
)

# Display values beside bars
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 2,
        bar.get_y() + bar.get_height() / 2,
        str(int(width)),
        va="center"
    )

plt.tight_layout()

# Save graph
output_file = output_dir / "COG_Functional_Category_Distribution.png"

plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.close()

print("COG functional distribution graph generated successfully.")
print("Saved at:", output_file)



