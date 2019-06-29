<<<<<<< HEAD
import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    dates = []
    winsorloss = []
    for row in csvreader:
        date = row[0]
        winorloss = row[1]

        dates.append(date)
        winsorloss.append(winorloss)

    print(date)
    print(winorloss)



=======
>>>>>>> a4f3069a0a8dd87488f330c5d2af775237b43968

