#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε εντολές της Python
#που ανοίγουν και κλείνουν αρχεία.
#χρησιμοποιούμε ένα αρχείο example_1.txt που βρίσκεται στον ιδιο φάκελο
#ανοίγουμε το αρχείο σε λειτουργία προσθήκης "a" προσθέτει στο τέλος τα νέα στοιχεία
#ανοίγουμε το αρχείο σε λειτουργία αποκλειστικής δημιουργίας "Χ"
#Δημιουργεί νέο αρχείο κενό. Εμφανίζει σφάλμα αν το αρχείο υπάρχει ήδη.
with open("example_1.txt","a",encoding="utf-8") as f:
    f.write("---εδώ ξεκινάει η προσθήκη των νέων στοιχείων --- ")
with open("example_1.txt",encoding="utf-8")as f:
    print(f.read())