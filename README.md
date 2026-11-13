# Comparative Genome Characterization of *Bacillus subtilis* 168 and *Bacillus licheniformis* DSM 13

## Project Overview

This project focuses on the comparative genome characterization of two bacterial species, *Bacillus subtilis* strain 168 and *Bacillus licheniformis* DSM 13, using computational bioinformatics approaches.

The study involves genome sequence analysis, nucleotide composition analysis, genome annotation, functional classification of protein-coding genes, nucleotide-level sequence comparison, and comparative enzyme analysis.

The primary aim is to investigate genomic characteristics, functional gene distributions, and similarities between the two bacterial genomes using publicly available genome sequences and bioinformatics tools.

## Objectives

- To analyze the basic genomic characteristics of both bacterial genomes.
- To calculate genome length, nucleotide composition, GC content, and AT content.
- To perform structural and functional genome annotation using Prokka.
- To identify protein-coding sequences and characterize annotated gene products.
- To classify annotated genes according to COG functional categories.
- To perform nucleotide-level comparative analysis using BLASTn.
- To compare enzyme-coding genes and EC number distributions between the two genomes.
- To interpret similarities and differences in their genomic and functional characteristics.

## Organisms Studied

| Feature | *B. subtilis* 168 | *B. licheniformis* DSM 13 |
|---|---|---|
| Organism | Bacillus subtilis | Bacillus licheniformis |
| Strain | 168 | DSM 13 |
| Genome type | Bacterial chromosome | Bacterial chromosome |
| Genome length | 4,215,606 bp | 4,222,336 bp |
| GC content | 43.51% | 46.20% |
| AT content | 56.49% | 53.80% |

**Reference genome accession for B. licheniformis DSM 13:** CP000002.1

## Methodology

### 1. Genome Sequence Collection

Complete genome sequences of *Bacillus subtilis* 168 and *Bacillus licheniformis* DSM 13 were obtained in FASTA format.

The downloaded sequences were organized into separate directories for primary and comparison genomes.

### 2. Genome Composition Analysis

Biopython was used to analyze the nucleotide composition of both genome sequences.

The following parameters were calculated:

- Total genome length
- Adenine (A) count
- Thymine (T) count
- Guanine (G) count
- Cytosine (C) count
- GC content
- AT content

The analysis was performed using Python and the Biopython library.

### 3. Genome Annotation Using Prokka

Structural and functional annotation was performed using Prokka (version 1.13.3).

Prokka was used to identify and annotate genomic features, including:

- Protein-coding sequences (CDS)
- Transfer RNA (tRNA)
- Ribosomal RNA (rRNA)
- Other genomic features
- Hypothetical proteins
- Annotated gene products

The annotation generated multiple output files, including GFF, GenBank, FASTA, protein sequence, nucleotide sequence, and annotation table files.

### 4. Functional Classification Using COG

Clusters of Orthologous Groups (COG) classification was performed to investigate the functional distribution of annotated protein-coding genes.

The COG2024 reference definition file was used for functional classification.

The analysis involved:
- Extraction of COG assignments from annotation results.
- Mapping of COG identifiers to functional categories.
- Classification of genes according to functional groups.
- Calculation of category-wise gene distributions.
- Visualization of functional classification results.

### 5. Comparative Genome Analysis Using BLASTn

BLASTn was used to perform nucleotide-level sequence comparison between the two bacterial genomes.

The analysis was conducted to identify local sequence similarities between the genomes.

The following parameters were evaluated:

- Number of BLAST alignments
- Percentage sequence identity
- Alignment length
- Query coverage
- Subject coverage
- Length-weighted sequence identity

Custom Python scripts were used to summarize and evaluate the BLAST output.

### 6. Comparative Enzyme Analysis

Enzyme-related annotations were extracted from the Prokka annotation results using Enzyme Commission (EC) numbers.

The analysis compared:

- Total protein-coding sequences.
- CDS with EC number assignments.
- Number of unique EC numbers.
- Enzyme annotation distributions between the two organisms.

Python scripts were used to process the annotation tables and generate comparative enzyme analysis results.

## Tools and Technologies

| Tool / Technology | Application |
|---|---|
| Python | Bioinformatics analysis and scripting |
| Biopython | Genome sequence analysis |
| Prokka 1.13.3 | Genome annotation |
| BLASTn | Nucleotide sequence comparison |
| COG2024 | Functional classification reference |
| Pandas | Data processing and analysis |
| NumPy | Numerical operations |
| Matplotlib | Graphical visualization |
| Conda | Environment and package management |
| VS Code | Python scripting and project organization |

## Results

### 1. Genome Composition Analysis

| Parameter | *B. subtilis* 168 | *B. licheniformis* DSM 13 |
|---|---:|---:|
| Genome length (bp) | 4,215,606 | 4,222,336 |
| Adenine (A) | 1,188,073 | 1,133,427 |
| Thymine (T) | 1,193,137 | 1,138,368 |
| Guanine (G) | 915,112 | 975,438 |
| Cytosine (C) | 919,284 | 975,103 |
| GC content (%) | 43.51 | 46.20 |
| AT content (%) | 56.49 | 53.80 |

**Observation:** Both genomes have similar genome sizes. However, *B. licheniformis* DSM 13 exhibits a higher GC content (46.20%) than *B. subtilis* 168 (43.51%).

### 2. Genome Annotation Results

| Annotation Parameter | *B. subtilis* 168 | *B. licheniformis* DSM 13 |
|---|---:|---:|
| Total CDS | 4,214 | 4,308 |
| Described CDS | 2,821 | 2,726 |
| Hypothetical proteins | 1,387 | 1,582 |
| Uncharacterized proteins | 6 | 0 |
| Gene assignments | 2,734 | 2,606 |
| COG assignments | 2,021 | 1,961 |
| EC assignments | 1,425 | 1,419 |

**Additional annotation features of B. licheniformis DSM 13:**

- Contigs: 1
- tRNA: 71
- rRNA: 21
- tmRNA: 1

**Observation:** *B. licheniformis* DSM 13 contains 94 more predicted CDS than *B. subtilis* 168. However, it also contains a greater number of hypothetical proteins.

### 3. COG Functional Classification

COG functional classification was performed using the COG2024 reference definitions.

For *B. subtilis* 168:

- Total COG-assigned CDS: 2,021
- Matched COG2024 identifiers: 2,021
- Unmatched identifiers: 0

The functional classification included categories such as:

- Information storage and processing
- Cellular processes and signaling
- Metabolism
- Poorly characterized functions

Examples of identified functional category counts in *B. subtilis* 168:

| COG Category | Gene Count |
|---|---:|
| A | 3 |
| B | 6 |
| C | 120 |
| D | 59 |
| E | 254 |
| F | 78 |
| G | 205 |
| H | 150 |

The COG classification results were also generated for *B. licheniformis* DSM 13.

### 4. BLASTn Comparative Analysis

The nucleotide-level comparison between the two genomes produced the following results:

| Parameter | Result |
|---|---:|
| Total BLAST alignments | 782 |
| Average sequence identity | 86.55% |
| Highest sequence identity | 100% |
| Average alignment length | 1,674.85 bp |
| Longest alignment | 19,915 bp |

**Genome Coverage Analysis**

| Parameter | Result |
|---|---:|
| Query coverage | 23.28% |
| Query covered bases | 981,530 bp |
| Subject coverage | 22.81% |
| Subject covered bases | 963,161 bp |
| Length-weighted identity | 83.1% |

**Observation:** BLASTn identified 782 local sequence alignments between the two genomes. The results demonstrate nucleotide-level similarities across the aligned regions. However, the coverage values indicate that the identified alignments represent only a portion of each genome.

### 5. Comparative Enzyme Analysis

Enzyme annotation was compared using EC numbers extracted from the Prokka annotation results.

| Parameter | *B. subtilis* 168 | *B. licheniformis* DSM 13 |
|---|---:|---:|
| Total CDS | 4,214 | 4,308 |
| EC-assigned CDS | 1,425 | 1,419 |
| Unique EC numbers | 795 | 798 |

**Observation:** Both organisms showed comparable numbers of EC-assigned coding sequences. *B. licheniformis* DSM 13 contained three more unique EC numbers than *B. subtilis* 168.

## Overall Conclusion

The comparative genome characterization of *Bacillus subtilis* 168 and *Bacillus licheniformis* DSM 13 provided insights into their genomic composition, structural and functional annotation, nucleotide-level similarities, and enzyme-associated gene distributions.

Both organisms exhibited similar genome sizes, although differences were observed in GC content and predicted protein-coding sequences.

Functional annotation and COG classification provided an overview of their gene functional profiles. BLASTn analysis identified nucleotide-level similarities between portions of the two genomes, while comparative enzyme analysis revealed broadly comparable EC annotation profiles.

Overall, this project demonstrates the application of computational bioinformatics approaches for bacterial genome characterization and comparative genomic analysis.

## Repository Structure

```text
Bacterial_Genome_Project/
│
├── 01_Genome_Sequences/
│   ├── B_subtilis_168_genome.fasta
│   └── Comparison_Genome/
│       └── B_licheniformis_DSM13_genome.fasta
│
├── 03_Genome_Annotation/
│   └── Prokka_Output_Final/
│
├── 04_Functional_Analysis/
│   ├── COG_Reference/
│   ├── COG classification results
│   └── Functional analysis outputs
│
├── 07_Comparative_Genome_Analysis/
│   ├── BLASTn results
│   ├── Genome coverage analysis
│   └── Comparative enzyme analysis
│
└── README.md
```

*Note: The structure above highlights the main project directories. Additional scripts, intermediate files, and output files are maintained in their respective folders.*

## Skills Demonstrated

- Bacterial genome sequence analysis
- Genome composition and GC content calculation
- Genome annotation
- Protein-coding gene analysis
- Functional classification using COG
- Nucleotide sequence comparison using BLASTn
- Enzyme annotation and EC number analysis
- Python-based bioinformatics scripting
- Data interpretation and visualization
- Computational comparative genomics

## Project Information

**Project Title:** Comparative Genome Characterization of *Bacillus subtilis* 168 and *Bacillus licheniformis* DSM 13

**Project Type:** Independent Bioinformatics Project

**Field:** Bacterial Genomics | Genome Annotation | Comparative Genomics | Functional Bioinformatics

**Author:** Subhalaxmi Sahoo

**Academic Background:** M.Sc. Bioinformatics
