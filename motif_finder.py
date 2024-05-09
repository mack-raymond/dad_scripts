from collections import defaultdict
import pandas as pd

score_cutoff = 100
input_score_table = "input_data/score_table.txt"
input_file = "input_data/145 bacterial proteins from svalbard.txt"
output_file = "output/output.csv"

# Load score lookup table for amino acids at each position
print(f"Loading score table: {input_score_table}")
score_table = {}

with open(input_score_table) as f:
    for line in f:
        amino_acid, *scores = line.strip().split("\t")
        print(f"{amino_acid}: {scores}")
        score_table[amino_acid] = list(map(int, scores))
print("Score table loaded successfully.")

# Function to compute the score of a 5-amino-acid sequence using the score table
def score_sequence(seq):
    assert len(seq) == 5, "Sequence length must be 5"
    score = 0
    for i, amino_acid in enumerate(seq):
        score += score_table.get(amino_acid, [0] * 5)[i]
    return score

# Function to highlight a sequence in the protein sequence with curly braces
def highlight_sequence_curly(protein_sequence, seq):
    return protein_sequence.replace(seq, f'[{seq}]')

# Initialize the results
results = defaultdict(list)

# Read the protein sequences
print(f"Reading protein sequences and scoring subsequences: {input_file}")
print("Using score cutoff:", score_cutoff)
with open(input_file) as f:
    lines = f.readlines()
    seq_name = None
    seq_content = None
    for line in lines:
        if line.startswith(">"):
            if seq_name:
                # Highlight subsequences for the last processed sequence (curly braces)
                highlighted_seq_curly = "".join(seq_content)
                for subseq, _, _ in sorted(results[seq_name], key=lambda x: x[2]):
                    highlighted_seq_curly = highlight_sequence_curly(highlighted_seq_curly, subseq)
                results[seq_name] = (highlighted_seq_curly, len(results[seq_name]))

            seq_name = line.strip()[:15]  # Truncate the sequence name to 15 characters
            seq_content = []
            print(f"Processing sequence: {seq_name}")
            continue

        # Store sequence content
        seq_content.extend(line.strip())

        # Search for all 5-amino-acid subsequences and compute scores
        for i in range(len(line.strip()) - 4):
            subseq = line.strip()[i:i + 5]
            score = score_sequence(subseq)
            if score >= score_cutoff:
                results[seq_name].append((subseq, score, (len(seq_content) - len(line.strip()) + i, len(seq_content) - len(line.strip()) + i + 5)))

# Highlight subsequences for the final sequence
if seq_name:
    highlighted_seq_curly = "".join(seq_content)
    for subseq, _, _ in sorted(results[seq_name], key=lambda x: x[2]):
        highlighted_seq_curly = highlight_sequence_curly(highlighted_seq_curly, subseq)
    results[seq_name] = (highlighted_seq_curly, len(results[seq_name]))

print("Scoring completed.")

# Prepare the results for output
print("Preparing output...")
output = []
for seq_name, (highlighted_seq_curly, num_hits) in results.items():
    output.append([num_hits, seq_name, highlighted_seq_curly])

# Create a DataFrame from the output
df = pd.DataFrame(output, columns=["hits", "sequence_name", "highlighted_sequence"])

# Save the DataFrame to a CSV file
df.to_csv(output_file, index=False)
print(f"Results saved to {output_file}.")
