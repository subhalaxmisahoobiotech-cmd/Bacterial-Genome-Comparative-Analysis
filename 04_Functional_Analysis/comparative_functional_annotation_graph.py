import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]
output_dir = project_dir / "05_Results_and_Graphs"

organisms = [
    "B. subtilis 168",
    "B. licheniformis DSM13"
]

features = [
    "Described CDS",
    "Hypothetical proteins",
    "Gene assignments",
    "COG assignments",
    "EC assignments"
]

subtilis = [2821, 1387, 2734, 2021, 1425]
licheniformis = [2726, 1582, 2606, 1961, 1419]

x = np.arange(len(features))
width = 0.35

plt.figure(figsize=(12, 6))

plt.bar(x - width/2, subtilis, width, label=organisms[0])
plt.bar(x + width/2, licheniformis, width, label=organisms[1])

plt.xticks(x, features, rotation=20, ha="right")
plt.ylabel("Number of CDS assignments")
plt.title("Comparative Functional Annotation of Bacillus Genomes")
plt.legend()

plt.tight_layout()

plt.savefig(
    output_dir / "Comparative_Functional_Annotation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Comparative functional annotation graph generated successfully.")