import os

# module for reading cs file

import csv

csvpath = os.path.join('.', 'resources', 'budget_data.csv')

print('opening',csvpath)

with open(csvpath) as csvfile:
    csvfile.readline()

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)



    count_total_months = 0
    sum_total_revenue = 0
    avg_change = 0
    total_revenue_change = 0
    greatest_increase_date = "IncreaseDate"
    greatest_increase_amt = 0
    greatest_decrease_date = "Dcrease"
    greatest_decrease_amt = 0
    prev_revenue = 0



    #  Each row is read as a row
    for row in csvreader:
            #print(row)
            count_total_months = count_total_months +1
            sum_total_revenue = sum_total_revenue + int(row[1])
            
            rev_increase = int(row[1]) - prev_revenue
            prev_revenue =  int(row[1])
            total_revenue_change = total_revenue_change + rev_increase
           
            if(rev_increase > greatest_increase_amt):
                greatest_increase_amt = rev_increase
                greatest_increase_date = row[0]

            if(rev_increase < greatest_decrease_amt):
                greatest_decrease_amt = rev_increase
                greatest_decrease_date = row[0]

    avg_change = total_revenue_change/count_total_months

    #create and open output file to write resuts to
    textfile_path = os.path.join(".", "analysis", "financialanalysis.txt")

    lines = []

    resultsfile = open(textfile_path, "w")

    #create the output
    lines.append("Financial Analysis")
    lines.append("----------------------------")
    lines.append("Total Months: "+str(count_total_months))
    lines.append("Total Revenue: $" + str(sum_total_revenue))
    lines.append("Average Revenue Change: $"+str(avg_change))
    lines.append("Greatest Increase in Revenue: "+greatest_increase_date + " ($" + str(greatest_increase_amt) +")")
    lines.append("Greatest Decrease in Revenue: "+greatest_decrease_date + " ($" + str(greatest_decrease_amt) +")")

     ##Write the output to file and console
    for line in lines:
        print(line)
        print(line,file=resultsfile)

    #new line
    print()

    #close the file
    resultsfile.close()   