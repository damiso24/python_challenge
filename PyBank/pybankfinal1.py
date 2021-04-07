import os
import csv

# set var to identify location of file
filepath = os.path.join('Resources', 'budget_data.csv')
# print (filepath)

# opens my file and lets cpu know file type 
with open(filepath) as csvfile:

    # reads and iterates through my file, recognizing the delimiters
    myreader = csv.reader(csvfile, delimiter=',')
    # print (myreader)

    # set var for my header so I can exclude from my output
    the_header = next(myreader)
    # print (the_header)

    # sets my file as a list.  This helps me find the length of my file/list
    thelist = list(myreader)

    # finds the length of my list.  each month = 1 row so all rows = total months
    total_months = len(thelist)
    # print (total_months)

    totalprofits = 0

    for row in thelist:
        totalprofits = totalprofits + int(row[1])

    # print (totalprofits)

    # Summary Table
    output = (
    f" \n"
    f"Financial Analysis \n"
    f"---------------------------- \n"
    f"Total Months: {total_months} \n"
    f"Total Profits: {totalprofits} \n"
    )
# Output our summary results to terminal
print(output)

# save output as a txt file
output_path = os.path.join(".", "Analysis", "financial_analysis.txt")
# print(output_path)

# with open(output_path, "w") as output_file:
    # print(output_file)
    # output_file.write(output)