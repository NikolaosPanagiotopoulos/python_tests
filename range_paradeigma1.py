print("θα εμφανιστούν όλοι οι ακέραιοι αριθμοί")
print("ανάμεσα σε 2 που θα δώσετε εσείς")
print("========================================\n")
#εισαγωγή 1ου και 2ου αριθμού από τον χρήστη
a=int(input("Δώσε τον 1ο αριθμό: "))
b=int(input("Δώσε τον 2ο αριθμό: "))
print("Ανάμεσα στο {} και στο {} υπάρχουν οι αριθμοί: ".format(a,b))
#Αύξηση του a κατά 1 για να μην συμπεριληφθει στον αρχικό  αριθμο
a=a+1
for i in range(a,b):
      print(i)
print("========================================\n")
print("Θα διατρέξουμε τη συμβολοσειρά \"Καλημέρα!\"")
str="Καλημέρα!"
i=1
for a in str:
    print("Χαρακτήρας {}: {}".format(i,a))
    i+=1
    
