# Specify the input and output file paths
input_file_path = "/Users/yash/Desktop/School/VSCode/hw5/hw5.csv"
output_file_path = "/Users/yash/Desktop/School/VSCode/hw5/hw5Text.csv"

# Open the input and output files
with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    # Write the header to the output file
    output_file.write("years,days\n")

    # Skip the header line in the input file
    next(input_file)

    # Process each line of the input file
    for line in input_file:
        # Split the line into columns
        columns = line.strip().split("\t")

        # Extract the relevant information and write it to the output file
        years = columns[0].split("-")[0]
        days = columns[3]
        # print(days)
        if (days != '–'):
            output_file.write(f"{years},{days}\n")
        else:
            print(years+","+days)

print("Reformatted data has been written to", output_file_path)