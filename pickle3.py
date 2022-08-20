#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε pickle 
#δηλαδη de-serialize ενός λεξικού example
#με τη συνάρτηση  load()
import pickle
example={
    "Χώρες":["Αυστρία","Βέλγιο","Βουλγαρία","Κροατία","Κύπρος"],
    "Πρωτεύουσες":["Βιέννη","Βρυξέλλες","Σόφια","Ζάγκρεμπ","Λευκωσία"]
    }
new_file=open('countries.pickle','rb')
new_example=pickle.load(new_file)
new_file.close()
print(new_example)
print(new_example==example)
print(type(new_example))
    
