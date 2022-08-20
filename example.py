#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε εντολές της Python
#που ανοίγουν και κλείνουν αρχεία.
try:
    f=open("example.txt",encoding="utf-8")
finally:
    f.close()
