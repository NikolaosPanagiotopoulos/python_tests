#Παράδειγμα 17
""" σε αυτό το παράδειγμα
θα χρησιμοποιήσουμε τελεστές για να κάνουμε πράξεις
στις συμβολοσειρές str
"""
name = "Jim"
surname = "Beam"
age=23
slogan="this ain't "+name+" "+surname+"!"
print(slogan)
#συμβολοσειρά πρότυπο
outstr="this bottle of {} {} is {} years old"
#παράθεση μεταβλητών σε σωστή σειρά
print(outstr.format(name,surname,age))
