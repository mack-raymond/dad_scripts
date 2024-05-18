from collections import defaultdict
import pandas as pd

score_cutoff = 100
input_score_table = "input_data/score_table.txt"
input_file = "input_data/145 bacterial proteins from svalbard.txt"
output_file = "output/output.csv"

# Load the score lookup table
score_table = {}
with open(input_score_table) as f:
    for line in f:
        amino_acid, *scores = line.strip().split("\t")
        score_table[amino_acid] = list(map(int, scores))

# Function to compute the score of a 5-amino-acid sequence
def score_sequence(seq):
    return sum(score_table.get(amino_acid, [0] * 5)[i] for i, amino_acid in enumerate(seq))

# Function to highlight a sequence in the protein sequence
def highlight_sequence(protein_sequence, seq):
    return protein_sequence.replace(seq, f'[{seq}]')

# Initialize the results
results = defaultdict(list)

# Read the protein sequences
with open(input_file) as f:
    seq_name = None
    seq_content = []
    for line in f:
        if line.startswith(">"):
            if seq_name:
                highlighted_seq = "".join(seq_content)
                for subseq, _, _ in sorted(results[seq_name], key=lambda x: x[2]):
                    highlighted_seq = highlight_sequence(highlighted_seq, subseq)
                results[seq_name] = (highlighted_seq, len(results[seq_name]))

            seq_name = line.strip()[:15]
            seq_content = []
            continue

        seq_content.extend(line.strip())
        for i in range(len(line.strip()) - 4):
            subseq = line.strip()[i:i + 5]
            score = score_sequence(subseq)
            if score >= score_cutoff:
                results[seq_name].append((subseq, score, (len(seq_content) - len(line.strip()) + i, len(seq_content) - len(line.strip()) + i + 5)))

if seq_name:
    highlighted_seq = "".join(seq_content)
    for subseq, _, _ in sorted(results[seq_name], key=lambda x: x[2]):
        highlighted_seq = highlight_sequence(highlighted_seq, subseq)
    results[seq_name] = (highlighted_seq, len(results[seq_name]))

# Prepare the results for output
output = [[num_hits, seq_name, highlighted_seq] for seq_name, (highlighted_seq, num_hits) in results.items()]

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(output, columns=["hits", "sequence_name", "highlighted_sequence"])
df.to_csv(output_file, index=False)
