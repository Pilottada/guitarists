"""
This module is focused on a single function that 
lets users add a new row on the csv of the 
guitarists/bands database.
"""
import csv
import pandas as pd
from checker import Check

check = Check()    
     
def add_element(g_or_b):
    """
    This function uses the user's input to the program 
    (which can be of either a band or a guitarist) with 
    the goal of adding it into the database.
    Before doing so, the function checks if the name is
    already inside the csv file. If it is all clear, the function
    will ask the user to specify if the name is the one of a guitarist
    or a band, and then ask for the other name. Finally it 
    writes both inputs in the csv file in the right columns.
    """
    db = pd.DataFrame(pd.read_csv('players_bands.csv'))
    if check.check_band(g_or_b):
        print("sorry, but " + g_or_b + "is already present in the database, thank you anyway")
    elif check.check_guitarist(g_or_b):
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