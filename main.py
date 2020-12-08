#! /usr/bin/env python3

from adder import add_element
from checker import check_guitarist, check_band
import argparse
import pandas as pd

db = pd.DataFrame(pd.read_csv('players_bands.csv'))
parser = argparse.ArgumentParser(description='this program will check if the name you put is inside our database of known guitarists or their bands. If the names have more than one space, plear wrap them around quotes ("")')
parser.add_argument("name", help = "input the name of a known guitarist or band")
parser.add_argument("-a", "--add", action = "store_true", help = "add a new guitarist or band")
parser.add_argument("-d", "--database", action = "store_true", help = "add a new guitarist or band")
args = parser.parse_args()
answer = args.name

    
if args.database:
    print("Now you can see by yourself if " + answer + " is present in our database!")
    print(db)
else:
    if args.add:
        add_element(answer)
    elif check_band(answer):
        print ("The guitar hero of", answer, "is", db["Players"].loc[db["bands"]==answer].values[0])
    elif check_guitarist(answer):
        print(answer, "is the guitar hero of ",db["bands"].loc[db["Players"]==answer].values[0] )
    else:
        response = input(answer + " is not present in our database. Would you like to add him? (y or n) -> ")
        if response == "y":
            add_element(answer)
        else:
            print("Thank you anyway")


