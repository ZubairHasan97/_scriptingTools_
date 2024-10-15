#!/bin/bash

read -p "Enter Uniprot ID file: " input_file
read -p "Enter Output fasta filename: " output_file
# header="Accept: text/plain; format=fasta"
base_url="https://rest.uniprot.org/uniprotkb/"

# Empty the output file if it already exists
> "$output_file"

while IFS= read -r uniprot_id; do
  url="${base_url}${uniprot_id}.fasta"
  
  # Append each sequence to the output file
  curl -S "$url" >> "$output_file"
  
  # Print a message after downloading each sequence
  echo "Downloaded: ${uniprot_id} and appended to ${output_file}"
done < "$input_file"

echo "Fasta sequences has been downloaded successfully -->> ${output_file}"

