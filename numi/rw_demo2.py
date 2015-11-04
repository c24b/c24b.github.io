
import csv
    
def read_csv(file='eggs.csv'):
    with open(file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        print ', '.join(row)
    return
    
def write_csv(filename="eggs.csv, data= ['Spam', 'Lovely Spam', 'Wonderful Spam']):
    #ecrire une liste de données dans un fichier avec pour séparateur ";"
    with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')
    spamwriter.writerow(data)
    return
