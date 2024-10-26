from main import *
import csv

with open('Servers.csv', 'a') as file:  # формируем csv файл
    CSwriter = csv.writer(file, dialect='excel')

    for i in parser():
        CSwriter.writerow(i)


