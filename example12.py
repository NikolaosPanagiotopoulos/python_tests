#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε εντολές της Python
#Θα χρησιμοποιήσουμε το os module της python για διαγραφή αρχείων
#με το os.remove()
#χρησιμοποιούμε ένα αρχείο example_2.txt που βρίσκεται στον ιδιο φάκελο
import os
if os.path.exists("example_2.txt"):
    os.remove("example_2.txt")
else:
    print("Το αρχείο δεν υπάρχει σε αυτό το directory")
