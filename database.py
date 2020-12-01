import csv
import guitarists
def database(dictionary):
	a_file = open("guitarists.csv","w")
    writer = csv.writer(a_file)
    for key, value in dictionary.items():
        writer.writerrow([key,value])
    a_file_close()
