from guitarists import list_of_guitarists
import pandas as pd

def csv_creator ():
    players = []
    bands = []
    for key, value in list_of_guitarists.items():
        players+=[key]
        bands+=[value]
    csv_players = pd.DataFrame(players, bands, columns = [ "Players"])
    csv_players = csv_players.reset_index()
    csv_players = csv_players.rename(columns={"index":"bands"})
    csv_players.to_csv ("players_bands.csv")