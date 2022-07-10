#σε αυτό το παράδειγμα θα πάρουμε ενα string και θα εμφανίσουμε το ίδιο αντεστραμμένο
#δηλαδή τους χαρακτήρες με αντίθετη σειρά από το τέλος προς την αρχή σε μία γραμμή
#Θα χρησιμοποιήσουμε την εντολή for με αρνητικό πρόσημο
#Θα συγκρίνουμε άν το αρχικό string ειναι ίδιο με το αντίστροφο του πχ serres 
#τότε θα εχουμε πσλίνδρομο
mystr="serres"
revstr=""
for i in range(len(mystr)-1,-1,-1):
    revstr+=mystr[i]   
print(revstr)

if mystr==revstr:
    print("Palindrome")
else:
    print("Non-Palindrome")

