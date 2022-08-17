#σε αυτό το παράδειγμα έχουμε δύο σύνολα sets
#Θα βρούμε τη διαφορά συνόλων Α-Β
#Θα χρησιμοποιήσουμε το difference()
#επιστρέφει ένα νέο σύνολο
print("---------Σύνολο 1 ---------------- ")
first_set={"a","b","c","d"}
print("Πρώτο σύνολο: ",first_set,"Πλήθος Στοιχειων: ",len(first_set))
print("---------Σύνολο 2 ---------------- ")
second_set={"a","b",1,2,3,4}
print("Δευτερο σύνολο: ",second_set,"Πλήθος Στοιχειων: ",len(second_set))
difference_A_B=first_set.difference(second_set)
difference_B_A=second_set.difference(first_set)
print("---------Έγινε η Διαφορά συνόλων---------------- ")
print("Το σύνολο διαφορά Α-Β ειναι : ",difference_A_B,"Πλήθος στοιχείων ",len(difference_A_B))
print("\n")
print("To σύνολο διαφορά Β-Α είναι : ",difference_B_A,"Πλήθος Στοιχειων: ",len(difference_B_A))





