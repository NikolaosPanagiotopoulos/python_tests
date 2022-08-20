#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε εντολές της Python
#που ανοίγουν και κλείνουν αρχεία.
#χρησιμοποιούμε ένα αρχείο example.txt που βρίσκεται στον ιδιο φάκελο

with open("example.txt",encoding="utf-8") as f:
   # print(f.read())
   # print("-----")
   # print(f.read(60))
    print("------")
    print(f.readline())
    
    
