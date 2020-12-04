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
        resp = input("Y or N")
        if resp =="Y":
            name_player = input("put the name of the guitarist")
            name_band = input("put the name of the band")
            with open('players_bands.csv', 'a') as newFile:
                newFileWriter = csv.writer(newFile)
                row = len(db)
                newFileWriter.writerow([row, name_player, name_band])
            print("Thank you for your contribution!")
        else: 
            print ("Thank you anyways, have a good day!")
       
    
                
                
# def check_band(band_name):
#     db = pd.DataFrame(pd.read_csv('players_bands.csv'))
#     for check in db.values:
#         if check[1] == band_name:
#             print("The guitar hero of {} is {}".format(band, guitarist))
#             return
#     print("Sorry, we don't know who is the guitar hero of {}".format(band_name))

# def adding_process():
#     print("Hi, it's time to add new guitarist players to this dataset, who would you like to add?")
#     g_name = input("Tell me the first and last name")
#     with open('innovators.csv', 'w', newline='') as file:
#             writer = csv.writer(file, delimiter='|')
#             writer.writerows(data_list)
            
#             if g_name == guitarist:
#                 print("This guitarist, member of {} is already in the database, thank you anyway".format(band))
#             else:
#                 b_name= input("tell me the name of the band")
#                 list_of_guitarists[g_name] = b_name
#                 return "The guitar hero of {} is {}".format(b_name, g_name)
                
#     print("Sorry, we don't know who is the guitar hero of {}".format(band_name))

    #giovanni fabris é un frocio e pure albi selfo

