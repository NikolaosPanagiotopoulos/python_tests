#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε pickle 
#δηλαδη serialize και de-serialize ενός λεξικού example

import pickle
example={
    "Χώρες":["Αυστρία","Βέλγιο","Βουλγαρία","Κροατία","Κύπρος"],
    "Πρωτεύουσες":["Βιέννη","Βρυξέλλες","Σόφια","Ζάγκρεμπ","Λευκωσία"]
    }
print(example)
print("---------δημιουργία του αρχείου countries.pickle------------------")
pickle_file=open('countries.pickle','wb')
pickle.dump(example,pickle_file)
pickle_file.close()
print("---το αρχειο περιέχει δυαδικά δεδομένα και βρίσκεται στον ιδιο φάκελο---")
