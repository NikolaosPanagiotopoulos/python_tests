#σε αυτό το παράδειγμα θα πάρουμε ενα string και θα  ελέγξουμε το αντεστραμμένο
#δηλαδή τους χαρακτήρες με αντίθετη σειρά από το τέλος προς την αρχή 
#άν το αρχικό string ειναι ίδιο με το αντίστροφο του πχ serres 
#τότε θα εχουμε πσλίνδρομο
#Θα προσθέσουμε τη βιβλιοθήκη sys για να εχουμε περισσότερες λειτουργίες
#Θα βάλουμε δύο δείκτες, εναν από την αρχή και
#εναν από το τέλος και θα συγκρίνουμε τους μισούς χαρακήρες με τους αλλους μισούς
import sys
mystr=input("Δώσε μία δική σου συμβολοσειρά: ")
revstr=""
mystr=mystr.lower()
mystr=mystr.replace(" ","")
palindrome=True
i=0

while(i<len(mystr)-1-i):
    if mystr[i]!=mystr[len(mystr)-1-i]:
        panlindrome=False
        break
    i+=1
if palindrome:
    print("palindrome")
else:
    print("non-palindrome")
print("User Input = {} bytes".format(sys.getsizeof(mystr)))
print("counter i = {} bytes".format(sys.getsizeof(i)))
print("boolean result = {} bytes".format(sys.getsizeof(palindrome)))


