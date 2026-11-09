import matplotlib.pyplot as plt
import os

# Organism names
organisms = ["B. subtilis 168", "B. licheniformis DSM 13"]

# Genome statistics
genome_size = [4215606, 4222336]
gc_content = [43.51, 46.20]
at_content = [56.49, 53.80]

# Output directory
output_dir = "05_Results_and_Graphs"
os.makedirs(output_dir, exist_ok=True)

# Graph 1: Genome size
plt.figure(figsize=(8, 5))
plt.bar(organisms, genome_size)
plt.title("Comparative Genome Size")
plt.ylabel("Genome Size (bp)")
plt.savefig(f"{output_dir}/Genome_Size_Comparison.png",
            dpi=300, bbox_inches="tight")
plt.close()

# Graph 2: GC content
plt.figure(figsize=(8, 5))
plt.bar(organisms, gc_content)
plt.title("Comparative GC Content")
plt.ylabel("GC Content (%)")
plt.ylim(0, 60)
plt.savefig(f"{output_dir}/GC_Content_Comparison.png",
            dpi=300, bbox_inches="tight")
plt.close()

# Graph 3: AT content
plt.figure(figsize=(8, 5))
plt.bar(organisms, at_content)
plt.title("Comparative AT Content")
plt.ylabel("AT Content (%)")
plt.ylim(0, 60)
plt.savefig(f"{output_dir}/AT_Content_Comparison.png",
            dpi=300, bbox_inches="tight")
plt.close()

print("All three comparative graphs generated successfully!")