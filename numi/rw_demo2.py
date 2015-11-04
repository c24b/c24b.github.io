def read_csv_file(filename):
    #lire une à une les lignes d'un fichier
    with open(filename, 'w') as f:
        for line in f:
            f.readline(line)
    return
    
def write_csv_file(filename, data):
    #ecrire une liste de données dans un fichier avec pour séparateur ";"
    with open(filename, 'w') as f:
        for line in data
            line = line.join(";")
            f.writeline(line)
    return
