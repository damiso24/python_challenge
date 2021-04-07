import os
import csv

# sets up my variable election data and tells computer where to find this file
csv_file_path = os.path.join(".", "Resources", "election_data.csv")
#print(csv_file_path)

# define and initialize variables
total_votes = 0


# Opens the file as a csv type
with open(csv_file_path) as csv_file:

    # Sets a variable that Reads the file and recognizes the commas as delimeters
    csv_reader_damiso = csv.reader(csv_file, delimiter=",")

    # read the header
    csv_header = next(csv_file)
    # print(csv_header)

    # read through each row in the csv file
    for every_row in csv_reader_damiso:
        # print(every_row[2])

        # increase total months by 1
        total_votes = total_votes + 1
        
# Set up our summary table
output = (
    f" \n"
    f"Election Results \n"
    f"-------------------- \n"
    f"Total Votes: {total_votes} \n"
    f"-------------------- \n"
    f"Khan: \n"
    f"Correy: \n"
    f"Li: \n"
    f"O'Tooley: \n"
    f"-------------------- \n"
    f"Winner: \n"
)

# Output our summary results to terminal
print(output)

# save output as a txt file
output_path = os.path.join(".", "Analysis", "election_analysis.txt")
#print(output_path)

with open(output_path, "w") as output_file:
    # print(output_file)
    output_file.write(output)