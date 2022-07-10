#σε αυτό το παράδειγμα θα πάρουμε ενα string και θα εμφανίσουμε το ίδιο αντεστραμμένο
#δηλαδή τους χαρακτήρες με αντίθετη σειρά από το τέλος προς την αρχή
mystr="Python"
print("First character: "+mystr[0])
print("String Length: "+str(len(mystr)))
print("Last character: "+mystr[len(mystr)-1])
print(mystr[len(mystr)-1])
position=len(mystr)-2
while(position!=0):
    print(mystr[position])
    position-=1
print(mystr[position])
