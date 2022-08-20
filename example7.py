#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε εντολές της Python
#που ανοίγουν και κλείνουν αρχεία.
#χρησιμοποιούμε ένα αρχείο example_1.txt που βρίσκεται στον ιδιο φάκελο
#φτιάχνουμε μία λίστα και την γράφουμε μέσα στο αρχείο με την μέθοδο
#writelines()
fruits=["Μήλο\n","Κεράσι\n","Πεπόνι\n","Μανταρίνι"]
with open("example_1.txt","w",encoding="utf-8") as f:
    f.writelines(fruits)
with open("example_1.txt",encoding="utf-8")as f:
    print(f.read())
