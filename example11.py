#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε εντολές της Python
#Θα χρησιμοποιήσουμε το os module της python για μετονομασία/διαγραφή αρχείων
#χρησιμοποιούμε ένα αρχείο example_4.txt που βρίσκεται στον ιδιο φάκελο
import os
if os.path.exists("example_4.txt"):
    os.rename("example_4.txt","example_2.txt")
else:
    print("Το αρχείο δεν υπάρχει σε αυτό το directory")
