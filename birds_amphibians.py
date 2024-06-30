# Script to create two files based on the content of the "file" file
# Each file will contain lines starting with ">" and containing either "birds" or "amphibians"
# The script will copy the sequence of letters below the ">" line to each corresponding file

# Open the input file
with open("all_apd2020.txt", "r") as input_file:
    # Open output files for birds and amphibians
    with open("birds.txt", "w") as birds_file, open("amphibians.txt", "w") as amphibians_file:
        # Iterate through each line in the input file
        for line in input_file:
            # Check if the line starts with ">" and contains the word "animals"
            if line.startswith(">") and "animals" in line:
                # Check if the line contains "birds"
                if "birds" in line:
                    # Write the line to the birds file
                    birds_file.write(line)
                    # Write the sequence of letters below the ">" line to the birds file
                    next_line = next(input_file)
                    birds_file.write(next_line)
                # Check if the line contains "amphibians"
                elif "amphibians" in line:
                    # Write the line to the amphibians file
                    amphibians_file.write(line)
                    # Write the sequence of letters below the ">" line to the amphibians file
                    next_line = next(input_file)
                    amphibians_file.write(next_line)

# Print message indicating successful file creation
print("Files 'birds.txt' and 'amphibians.txt' created successfully.")

