#σε αυτό το παράδειγμα έχουμε δύο σύνολα sets
#Θα βρούμε τη συμμετρική διαφορά συνόλων Α-Β
#Θα χρησιμοποιήσουμε το symmetric_difference()
#θα επιστρεψει ενα νέο σύνολο που θα περιέχει
#μόνο όσα στοιχεία δεν ειναι κοινά στα δύο σύνολα
print("---------Σύνολο 1 ---------------- ")
first_set={"a","b","c","d"}
print("Πρώτο σύνολο: ",first_set,"Πλήθος Στοιχειων: ",len(first_set))
print("---------Σύνολο 2 ---------------- ")
second_set={"a","b",1,2,3,4}
print("Δευτερο σύνολο: ",second_set,"Πλήθος Στοιχειων: ",len(second_set))
sym_difference_AB=first_set.symmetric_difference(second_set)
print("---------Έγινε η Συμμετρική Διαφορά συνόλων---------------- ")
print("Το σύνολο συμμετρική διαφορά Α-Β ειναι : ",sym_difference_AB,"Πλήθος Στοιχειων: ",len(sym_difference_AB))
print("To σύνολο1 είναι : ",first_set,"Πλήθος Στοιχειων: ",len(first_set))
print("To σύνολο2 είναι : ",second_set,"Πλήθος Στοιχειων: ",len(second_set))






