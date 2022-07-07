#Σε αυτό το παράδειγμα θα αντικαταστήσουμε τα κενά με \n κάθε λέξη αλλάζει γραμμή
string = """In computer programming, a string is traditionally a sequence of
characters, either as a literal constant or as some kind of variable. The
latter may allow its elements to be mutated and the length changed, or it may
be fixed (after creation). A string is generally considered as a data type
and is often implemented as an array data structure of bytes (or words) that
stores a sequence of elements, typically characters, using some character
encoding. String may also denote more general arrays or other sequence (or
list) data types and structures."""
print(string.count(" "))
string2=string.replace(" ","\n")
print(string2)
#1 μετατροπή σε μικρά
processed_string=string.lower()
#2.1 απαλοιφή κομμάτων και τελειών
processed_string=processed_string.replace(",","")
processed_string=processed_string.replace(".","")
#2.2 σπαλοιφή παρενθέσεων
processed_string=processed_string.replace("(","")
processed_string=processed_string.replace(")","")
#3 αντικατάσταση κενών με νέα γραμμή
processed_string=processed_string.replace(" ","\n")
print(processed_string)
