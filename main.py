import whois
from datetime import datetime

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words
    
def query(url): 
    return whois.query(url)

domeny = readFile("domeny.txt")

raport = []
for url in domeny: 
    domain = query(url)
    owner = domain.registrant
    creationDate = domain.creation_date
    toExpire = domain.expiration_date - datetime.now()
    raport.append("Domena: " + domain.name + "; właściciel: " + owner + "; data stworzenia: " + str(creationDate) + "; czas do wygaśnięcia: " + str(toExpire))

with open('raport.txt', 'a') as f:
    f.writelines('\n'.join(raport))


