#Import Biopython modules
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import molecular_weight

#Reading AA fasta file
usr_input = input("Enter the file path: ")
fasta_sequences = SeqIO.parse(usr_input, "fasta")

# Define the minimum and maximum molecular weight range
def set_MW_range():
  min_weight = int(input("Enter the minimum molecular weight: "))
  max_weight = int(input("Enter the maximum molecular weight: "))
  return min_weight, max_weight

min_weight, max_weight = set_MW_range()

def filter_aa_seqs_by_mw(sequences, min_wt, max_wt):
  for sequence in sequences:
    # print(sequence.description)
    weight_aa = molecular_weight(sequence.seq, seq_type='protein')
    if min_wt <= weight_aa <= max_wt:
      print(">", sequence.id,"MW:", round(weight_aa/1000, 2), "KDa")
      print("Seq:",sequence.seq)

filter_aa_seqs_by_mw(fasta_sequences, min_weight, max_weight)
