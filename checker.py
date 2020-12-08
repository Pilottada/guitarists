import csv
import pandas as pd

def check_guitarist(guitar_player):
    db = pd.DataFrame(pd.read_csv('players_bands.csv'))
    if guitar_player in db["Players"].values:
        return True
    return False
               
                              
def check_band(band_name):
    db = pd.DataFrame(pd.read_csv('players_bands.csv'))
    if band_name in db["bands"].values:
        return True
    return False