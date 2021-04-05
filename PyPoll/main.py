import os
import csv

#sets up my variable election data and tells computer where to find this file
election_data = os.path.join(".", "Resources", "election_data.csv")

print(election_data)

#Opens the file as a csv type
#with open(election_data) as csv_file:

#Sets a variable that Reads the file and recognizes the commas as delimeters
    #csv_reader = csv.reader(csv_file, delimiter=",")
    