#σε αυτό το παράδειγμα θα πάρουμε ενα string και θα εμφανίσουμε το ίδιο αντεστραμμένο
#δηλαδή τους χαρακτήρες με αντίθετη σειρά από το τέλος προς την αρχή σε μία γραμμή
#Θα χρησιμοποιήσουμε την εντολή for με αρνητικό πρόσημο
#Θα συγκρίνουμε άν το αρχικό string ειναι ίδιο με το αντίστροφο του πχ serres 
#τότε θα εχουμε πσλίνδρομο
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

