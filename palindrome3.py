#σε αυτό το παράδειγμα θα πάρουμε ενα string και θα εμφανίσουμε το ίδιο αντεστραμμένο
#δηλαδή τους χαρακτήρες με αντίθετη σειρά από το τέλος προς την αρχή σε μία γραμμή
#Θα συγκρίνουμε άν το αρχικό string ειναι ίδιο με το αντίστροφο του πχ serres 
#τότε θα εχουμε πσλίνδρομο
#Θα προσθέσουμε τη βιβλιοθήκη sys για να εχουμε περισσότερες λειτουργίες
import sys
mystr=input("Δώσε μία δική σου συμβολοσειρά: ")
revstr=""
mystr=mystr.lower()
mystr=mystr.replace(" ","")
for i in range(len(mystr)-1,-1,-1):
    revstr+=mystr[i]   
print("Η αντίστροφη συμβολοσειρά χωρίς κενά και όλα μικρά είναι: ",revstr)

if mystr==revstr:
    print("Palindrome")
else:
    print("Non-Palindrome")
print("User Input = {} bytes".format(sys.getsizeof(mystr)))
print("reverse input = {} bytes".format(sys.getsizeof(revstr)))
print("counter i = {} bytes".format(sys.getsizeof(i)))

