#σε αυτό το παράδειγμα θα ενώσουμε δύο σύνολα sets
#και θα αποθηκευτει η αλλαγή στο 1ο σύνολο
#Θα χρησιμοποιήσουμε το update()
print("---------Σύνολο 1 ---------------- ")
first_set={"a","b","c","d","e","f","g"}
print("Πρώτο σύνολο: ",first_set,"Πλήθος Στοιχειων: ",len(first_set))
print("---------Σύνολο 2 ---------------- ")
second_set={"John",1}
print("Δευτερο σύνολο: ",second_set,"Πλήθος Στοιχειων: ",len(second_set))
first_set.update(second_set)
print("Το νεο σύνολο 1 ειναι τώρα: ",first_set)





