from collections import defaultdict
import pandas as pd

score_cutoff = 80
input_score_table = "input_data/score_table.txt"
input_file = "input_data/sequence.txt"
output_file = "output/output.csv"

# Load score lookup table for amino acids at each position
print(f"Loading score table: {input_score_table}")
score_table = {}

with open(input_score_table) as f:
    for line in f:
        amino_acid, *scores = line.strip().split(",")
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

# Initialize the results
results = defaultdict(list)

# Read the protein sequences
print(f"Reading protein sequences and scoring subsequences: {input_file}")
print("Using score cutoff:", score_cutoff)
with open(input_file) as f:
    lines = f.readlines()
    seq_name = None
    for line in lines:
        if line.startswith(">"):
            seq_name = line.strip()[:15]  # Truncate the sequence name to 15 characters
            print(f"Processing sequence: {seq_name}")
            continue

        # Search for all 5-amino-acid subsequences and compute scores
        for i in range(len(line.strip()) - 4):
            subseq = line.strip()[i:i + 5]
            score = score_sequence(subseq)
            if score >= score_cutoff:
                results[seq_name].append((subseq, score, (i, i + 5)))

print("Scoring completed.")

# Prepare the results for output
print("Preparing output...")
output = []
for seq_name, matches in results.items():
    for subseq, score, pos in matches:
        output.append([len(matches), seq_name, subseq])

# Create a DataFrame from the output
df = pd.DataFrame(output, columns=["No. of Hits", "Seq Name", "Sequence"])

# Save the DataFrame to a CSV file
df.to_csv(output_file, index=False)
print(f"Results saved to {output_file}.")
