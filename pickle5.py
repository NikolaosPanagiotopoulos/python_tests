#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε pickle 
#δηλαδη de-serialize ενός λεξικού example
#με τη συνάρτηση  loads()
#που δέχεται ως ορισμα μία συμβολοσειρά
import pickle
example={
    "Χώρες":["Αυστρία","Βέλγιο","Βουλγαρία","Κροατία","Κύπρος"],
    "Πρωτεύουσες":["Βιέννη","Βρυξέλλες","Σόφια","Ζάγκρεμπ","Λευκωσία"]
    }
print("Τα αρχικά δεδομένα είναι: \n",example)
pickled_example=pickle.dumps(example)
print("Μετά το Pickling:\n",pickled_example)
unpickled_example=pickle.loads(pickled_example)
print('Μετά το Unpickling:\n',unpickled_example)
