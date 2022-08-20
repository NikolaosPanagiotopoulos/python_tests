#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε εντολές της Python
#που ανοίγουν και κλείνουν αρχεία.
#χρησιμοποιούμε ένα αρχείο example_1.txt που βρίσκεται στον ιδιο φάκελο

with open("example_1.txt","w",encoding="utf-8") as f:
    f.write("Πρώτη γραμμή\n")
    f.write("Δεύτερη γραμμή\n\n")
    f.write("Τρίτη γραμμή\n")
    f.write("Τέταρτη γραμμή\n")
    f.write("Πέμπτη γραμμή\n")
with open("example_1.txt",encoding="utf-8")as f:
    print(f.read())
