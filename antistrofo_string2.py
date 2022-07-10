#σε αυτό το παράδειγμα θα πάρουμε ενα string και θα εμφανίσουμε το ίδιο αντεστραμμένο
#δηλαδή τους χαρακτήρες με αντίθετη σειρά από το τέλος προς την αρχή σε μία γραμμή
mystr="Python"
revstr=""
revstr+=mystr[len(mystr)-1]
position=len(mystr)-2
while(position!=0):
    revstr+=mystr[position]
    position-=1
revstr+=mystr[position]    
print(revstr)
