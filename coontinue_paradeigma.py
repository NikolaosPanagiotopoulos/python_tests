#σε αυτό το παράδειγμα θα χρησιμοποιήσουομε την continue
#αν κάποιος δώσει ως είσοδο το 0 θα το αγνοήσει και θα πάει στους αλλους αριθμούς
print("Θα δώσεις 10 αριθμούς και θα υπολογίσω το γινόμενο τους.")
print("αν κάποιος από τους αριθμούς είναι το 0 θα το αγνοήσει στον υπολογισμό")
print("=======================================================================\n")
ginomeno=1
for i in range(1,11):
    a=int(input("Δώσε τον {}-ο αριθμό ".format(i)))
    if a==0:
        continue
    ginomeno*=a
print("το γινόμενο των αριθμών που έδωσες (χωρίς το 0) είναι: ",ginomeno)
    
