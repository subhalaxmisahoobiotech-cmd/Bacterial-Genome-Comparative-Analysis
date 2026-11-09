
import pandas as pd

file_path = (
    "07_Comparative_Genome_Analysis/"
    "B_subtilis_vs_B_licheniformis_BLAST.tsv"
)

columns = [
    "Query_ID", "Subject_ID", "Identity",
    "Length", "Mismatches", "Gaps",
    "Q_Start", "Q_End", "S_Start", "S_End",
    "E_value", "Bit_Score"
]

df = pd.read_csv(file_path, sep="\t", names=columns)


def merged_coverage(start, end):
    intervals = sorted(
        (min(a, b), max(a, b))
        for a, b in zip(start, end)
    )

    if not intervals:
        return 0

    total = 0
    current_start, current_end = intervals[0]

    for next_start, next_end in intervals[1:]:
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            total += current_end - current_start + 1
            current_start, current_end = next_start, next_end

    total += current_end - current_start + 1
    return total


query_length = 4215606
subject_length = 4222336

query_covered = merged_coverage(df["Q_Start"], df["Q_End"])
subject_covered = merged_coverage(df["S_Start"], df["S_End"])

query_coverage = query_covered / query_length * 100
subject_coverage = subject_covered / subject_length * 100

weighted_identity = (
    (df["Identity"] * df["Length"]).sum()
    / df["Length"].sum()
)

print("GENOME ALIGNMENT COVERAGE")
print("-------------------------")
print("Query genome coverage:",
      round(query_coverage, 2), "%")
print("Subject genome coverage:",
      round(subject_coverage, 2), "%")
print("Query bases covered:", query_covered)
print("Subject bases covered:", subject_covered)
print("Length-weighted alignment identity:",
      round(weighted_identity, 2), "%")

print("\nNote: Coverage is based on the union of BLAST alignment")
print("intervals. Overlapping query or subject intervals are")
print("counted only once within their respective genomes.")
