import csv
from guitarists import list_of_guitarists

def database(dictionary):
        a_file = open("guitarists.csv","w")
        writer = csv.writer(a_file)
        for key, value in dictionary.items():
            writer.writerow([key,value])
        a_file.close()

database(list_of_guitarists)
