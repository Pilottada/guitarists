"""
This module applies all the functions 
created in the other modules of the package
to let the user interact with the database of 
guitarists and bands.

We used the argparse module to parse the 
command line and add 1 positional argument and 2 optional ones.
The "name" positional argument asks for the name of a known guitarist
or band, which will be used to check its presence in the database 
or give the user the ability to add it inside of it.

Then we added the "--add" optional argument that lets the user 
go straight to the process of adding the name of the guitarist 
and band into the database.

Finally, the last optional argument "--database" gives the user
the chance to see the database by themselves on the command line
so they can check the presence of the name they put as input

The two optional arguments are mutually exclusive since they have
opposite objectives.
"""
#! /usr/bin/env python3

from adder import add_element
from checker import Check
import argparse
import pandas as pd

check = Check()

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
    elif check.check_band(answer):
        print ("The guitar hero of", answer, "is", db["Players"].loc[db["bands"]==answer].values[0])
    elif check.check_guitarist(answer):
        print(answer, "is the guitar hero of ",db["bands"].loc[db["Players"]==answer].values[0] )
    else:
        response = input(answer + " is not present in our database. Would you like to add him? (y or n) -> ")
        if response == "y":
            add_element(answer)
        else:
            print("Thank you anyway")


