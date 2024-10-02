# Importing BioPython Seq module for sequence manipulation
from Bio.SeqUtils import molecular_weight

#Calculating MW of Nucleotide Sequences/DNA
def filter_sequences_by_molecular_weight(sequences, min_weight, max_weight):
    filtered_sequences = []
    filtered_weights = []
    my_dict = {}
    for sequence in sequences:
        # Calculate molecular weight
        weight = molecular_weight(sequence)
        # Check if weight falls within the specified range
        if min_weight <= weight <= max_weight:
            filtered_sequences.append(sequence)
            filtered_weights.append(weight)
    for i in range(len(filtered_sequences)):
        my_dict[filtered_sequences[i]] = filtered_weights[i]
    return my_dict

# Example usage
if __name__ == "__main__":
    # Sample nucleotide sequences
    sequences = [
        "ATGCATGCATGC",
        "ATGCGCATGC",
        "ATGCCCGCATGC",
        "ATGCCG",
        "ATGCATGC",
    ]

    # input your sequences
    def take_sequences(seq):
      input_seq = input("Enter the sequence: ")
      seq.append(input_seq)
      return

    take_sequences(sequences)

    # Define the minimum and maximum molecular weight range
    def set_molecular_weight_range():
        min_weight = int(input("Enter the minimum molecular weight: "))
        max_weight = int(input("Enter the maximum molecular weight: "))
        return min_weight, max_weight

    min_weight, max_weight = set_molecular_weight_range()

    # Filter sequences by molecular weight
    filtered_sequences = filter_sequences_by_molecular_weight(sequences, min_weight, max_weight)

    # Print filtered sequences
    print("Filtered sequences with molecular weight between", min_weight, "and", max_weight)
    for sequence, weight in filtered_sequences.items():
        print(f"Sequence: {sequence}, {round(weight/1000, 2)} KDa")

    print(filtered_sequences)
