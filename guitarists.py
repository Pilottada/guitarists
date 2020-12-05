import csv
import pandas as pd

list_of_guitarists = {'Eric Clapton':'Cream',
'Jimmy Page': 'Led Zeppelin',
'Keith Richards': 'Rolling Stones',
'Eddie Van Halen': 'Van Halen',
'David Gilmour': 'Pink Floyd',
'Angus Young': 'AD/DC',
'Brian May': 'Queen',
'Johnny Ramone': 'Ramones',
'Tom Morello': 'Rage Against the Machine',
'Slash': "Guns'n Roses",
'Jim Root': 'Slipknot',
'Kirk Hammet': 'Metallica'
}

def check_guitarist(guitar_player):
    db = pd.DataFrame(pd.read_csv('players_bands.csv'))
    if guitar_player in db["Players"].values:
        print(guitar_player, "is the guitar hero of ",db["bands"].loc[db["Players"]==guitar_player].values[0] )
       
    else:
        print("Sorry, {} does not seem to be a known guitarist".format(guitar_player))
        print ("Would you like to add a voice to our database?")
        resp = input("Y or N -> ")
        if resp =="Y":
            name_player = input("Put here the name of the guitarist -> ")
            name_band = input("Put here the name of the band -> ")
            with open('players_bands.csv', 'a') as newFile:
                newFileWriter = csv.writer(newFile)
                row = len(db)
                newFileWriter.writerow([row, name_player, name_band])
            print("Thank you for your contribution!")
        else: 
            print ("Thank you anyways, have a good day!")
       
    
                
                
def check_band(band_name):
    db = pd.DataFrame(pd.read_csv('players_bands.csv'))
    if band_name in db["bands"].values:
        print ("The guitar hero of", band_name, "is", db["Players"].loc[db["bands"]==band_name].values[0]) 
    
    else:
        print ("Sorry, {} does not seem to be a known band".format(band_name))
        print ("Would you like to add a voice to our database?")
        resp = input ("Y or N -> ")
        if resp == "Y":
            name_band = input ("Put here the name of the band -> ")
            name_player = input("Put here the name of the guitarist -> ")
            with open('players_bands.csv', 'a') as newFile:
                newFileWriter = csv.writer(newFile)
                row = len(db)
                newFileWriter.writerow([row, name_band, name_player])
            print("Thank you for your contribution!")
        else: 
            print ("Thank you anyways, have a good day!")





