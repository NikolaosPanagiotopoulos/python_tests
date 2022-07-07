#Σε αυτό το παράδειγμα θα αφαιρέσουμε κενά από ενα string
string2 = """ In  computer programming, a string is traditionally
a sequence  of characters, either as a literal constant or as some kind
of variable. The latter  may allow  its elements to be mutated and the
length changed, or it may be fixed (after creation). A string is
generally considered as a data type and is often implemented as an array
data  structure of bytes (or words)  that stores a sequence of elements,
typically  characters, using  some character encoding. String may also
denote more general arrays or other sequence (or list) data types  and
structures. """
#0.Αρχική καταμέτρηση κενών
print("word count before string cleansing")
print(string2.count(" "))
#1.αφαίρεση αρχικών και τελικών κενών
string2=string2.strip()
print("μέτρηση κενών μετά από αφαίρεση αρχικών και τελικών κενών")
print(string2.count(" "))
#2.αντικατάσταση διπλών κενών με μονά κενά
string2=string2.replace("  "," ")
print("μέτρηση κενών μετά από την αντικατάσταση διπλών κενών με μονά")
print(string2.count(" "))
#3. Τελική καταμέτρηση
print("word count after string cleansing")
print(string2.count(" ")+1)

