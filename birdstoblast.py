import requests

def read_sequences_from_file(filename):
    sequences = []
    with open('birds.txt', 'r') as file:
        sequence_id = None
        sequence = ""
        for line in file:
            if line.startswith(">"):  # Found a sequence ID
                if sequence_id is not None:  # Save the previous sequence
                    sequences.append((sequence_id, sequence))
                sequence_id = line.strip()[1:]  # Remove ">" and newline
                sequence = ""  # Reset sequence string for the new sequence
            else:  # Sequence data
                sequence += line.strip()
        # Append the last sequence after the loop ends
        if sequence_id is not None:
            sequences.append((sequence_id, sequence))
    return sequences

def perform_blast(sequence):
    # Define BLAST URL and parameters
    blast_url = "https://www.uniprot.org/blast/"
    params = {
        "seq": sequence,
        "output": "tab",
        "format": "fasta",
        "identity": "90",  # Filter for sequences with >90% identity
    }
    # Perform BLAST request
    response = requests.post(blast_url, params=params)
    if response.ok:
        return response.text
    else:
        print("Error performing BLAST request:", response.text)
        return None

def filter_results(blast_results):
    filtered_results = []
    lines = blast_results.split('\n')
    for line in lines:
        if line.startswith("#"):  # Skip comment lines
            continue
        fields = line.split('\t')
        # Check if identity percentage is greater than 90%
        if float(fields[2]) > 90:
            filtered_results.append(line)
    return '\n'.join(filtered_results)

def write_results_to_file(filename, results):
    with open(filename, 'w') as file:
        file.write(results)

def main():
    input_filename = "birds.txt"
    output_filename = "result_blast.txt"

    # Read sequences from file
    sequences = read_sequences_from_file(input_filename)

    # Perform BLAST for each sequence
    for sequence_id, sequence in sequences:
        print(f"Performing BLAST for sequence ID: {sequence_id}")
        blast_result = perform_blast(sequence)
        if blast_result:
            # Filter results for identities >90%
            filtered_result = filter_results(blast_result)
            if filtered_result:
                # Write filtered results to file
                write_results_to_file(output_filename, filtered_result)
                print(f"Filtered BLAST results written to {output_filename}")

if __name__ == "__main__":
    main()


