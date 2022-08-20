#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε pickle 
#δηλαδη serialize και de-serialize ενός λεξικού example
#με τη συνάρτηση  dumps()
import pickle
example={
    "Χώρες":["Αυστρία","Βέλγιο","Βουλγαρία","Κροατία","Κύπρος"],
    "Πρωτεύουσες":["Βιέννη","Βρυξέλλες","Σόφια","Ζάγκρεμπ","Λευκωσία"]
    }
print(example)
pickled_example=pickle.dumps(example)
print(pickled_example)

    
