import csv
import pandas as pd
from checker import check_guitarist, check_band
    
     
def add_element(g_or_b):
    db = pd.DataFrame(pd.read_csv('players_bands.csv'))
    if check_band(g_or_b):
        print("sorry, but " + g_or_b + "is already present in the database, thank you anyway")
    elif check_guitarist(g_or_b):
        print("sorry, but " + g_or_b + " is already present in the database, thank you anyway")
    else:
        name1 = input("Is he a guitarist or is it a band (g or b) -> ")
        if name1 == "b":
            name2 = input("Now enter the name of the guitarist -> ")
            with open('players_bands.csv', 'a') as newFile:
                newFileWriter = csv.writer(newFile)
                row = len(db)
                newFileWriter.writerow([row, g_or_b, name2])
            print("Thank you for your contribution!")
        elif name1 == "g":
            name2 = input("Now enter the name of the band -> ")
            with open('players_bands.csv', 'a') as newFile:
                newFileWriter = csv.writer(newFile)
                row = len(db)
                newFileWriter.writerow([row, name2, g_or_b])
            print("Thank you for your contribution!")
        else:
            print("you need to input either g or b")
            exit()