
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

project_dir = Path(__file__).resolve().parents[1]

output_dir = project_dir / "05_Results_and_Graphs"
output_dir.mkdir(exist_ok=True)

organisms = [
    "B. subtilis 168",
    "B. licheniformis DSM13"
]

cds_with_ec = [1425, 1419]
unique_ec = [795, 798]

x = np.arange(len(organisms))
width = 0.35

plt.figure(figsize=(9, 6))

plt.bar(
    x - width / 2,
    cds_with_ec,
    width,
    label="CDS with EC numbers"
)

plt.bar(
    x + width / 2,
    unique_ec,
    width,
    label="Unique EC numbers"
)

plt.xticks(x, organisms)
plt.ylabel("Number of assignments")
plt.title("Comparative Enzyme Annotation")
plt.legend()
plt.tight_layout()

plt.savefig(
    output_dir / "Comparative_Enzyme_Annotation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Comparative enzyme graph generated successfully.")
