
import matplotlib.pyplot as plt
from pathlib import Path

# Project directories
project_dir = Path(__file__).resolve().parent.parent
output_dir = project_dir / "05_Results_and_Graphs"
output_dir.mkdir(exist_ok=True)

# Functional annotation data
categories = [
    "Functionally described",
    "Hypothetical proteins",
    "Uncharacterized proteins"
]

counts = [2821, 1387, 6]

# Graph 1: Functional classification
plt.figure(figsize=(9, 6))

bars = plt.bar(categories, counts)

plt.title("Functional Classification of CDS in Bacillus subtilis 168")
plt.xlabel("Protein Categories")
plt.ylabel("Number of CDS")
plt.xticks(rotation=15, ha="right")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height)}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(
    output_dir / "CDS_Functional_Classification.png",
    dpi=300
)
plt.close()


# Graph 2: Annotation evidence
annotation_types = [
    "Gene names",
    "COG assignments",
    "EC numbers"
]

annotation_counts = [2734, 2021, 1425]

plt.figure(figsize=(8, 6))

bars = plt.bar(annotation_types, annotation_counts)

plt.title("Functional Annotation Evidence in Bacillus subtilis 168")
plt.xlabel("Annotation Types")
plt.ylabel("Number of CDS")

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height)}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig(
    output_dir / "Annotation_Evidence.png",
    dpi=300
)
plt.show()

print("Both graphs generated successfully.")
print("Saved in:", output_dir)
