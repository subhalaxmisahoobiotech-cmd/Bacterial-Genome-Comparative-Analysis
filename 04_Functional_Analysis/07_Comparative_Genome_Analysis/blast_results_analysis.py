
import pandas as pd
import os

file_path = (
    "07_Comparative_Genome_Analysis/"
    "B_subtilis_vs_B_licheniformis_BLAST.tsv"
)

columns = [
    "Query_ID", "Subject_ID", "Percentage_Identity",
    "Alignment_Length", "Mismatches", "Gap_Openings",
    "Query_Start", "Query_End", "Subject_Start",
    "Subject_End", "E_value", "Bit_Score"
]

df = pd.read_csv(file_path, sep="\t", names=columns)

print("BLASTn RESULTS SUMMARY")
print("----------------------")

print("Total alignments:", len(df))
print("Average percentage identity:",
      round(df["Percentage_Identity"].mean(), 2), "%")
print("Highest percentage identity:",
      round(df["Percentage_Identity"].max(), 2), "%")
print("Average alignment length:",
      round(df["Alignment_Length"].mean(), 2), "bp")
print("Longest alignment:",
      df["Alignment_Length"].max(), "bp")

print("\nTop 10 BLAST alignments:")
print(
    df.sort_values("Bit_Score", ascending=False)
      .head(10)
      .to_string(index=False)
)

output_path = (
    "07_Comparative_Genome_Analysis/"
    "BLAST_results_summary.csv"
)

df.to_csv(output_path, index=False)

print("\nResults saved:", output_path)
