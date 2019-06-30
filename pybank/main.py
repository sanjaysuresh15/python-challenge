import os
import csv
budget_csv = os.path.join('..','Resources','budget_data.csv',)
with open(budget_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(budget_csv[0])
    
