#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε import requests που είναι μία
#εναλλακτική βιβλιοθήκη αντί για την urlib.requests
#Αρχικά εγκαταστήσαμε χειροκίνητα τη βιβλιοθήκη requests μέσω του pip
#θα χρησιμοποιήσουμε την requests.get(URL)
#δημιουργείται ένα αντικείμενο Response 
#που περιέχει τις πληροφορίες ως ιδιότητες και μεθόδους
import requests
req=requests.get("https://www.wikipedia.com/robots.txt")
print('Οι πρώτοι 100 χαρακτήρες')
print(req.text[0:100])
print('\n η κωδικοποίηση είναι:',req.encoding)
print('Η ιδιότητα text επιστρέφει κείμενο τύπου: ',type(req.text))
with open("myfile2.txt",encoding="utf-8",mode="w") as my_file:
    my_file.write(req.text)
         
