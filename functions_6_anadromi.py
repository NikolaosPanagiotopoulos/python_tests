#σε αυτό το παράδειγμα θα δημιουργήσουμε μία συνάρτηση παραγοντικού
#η οποία κάνει αναδρομή και καλεί τον εαυτό της.
def paragontiko(n):
    if n==0 or n==1:
        return 1
    else:
        parag=n*paragontiko(n-1)
    return parag
n=int(input("δώστε εναν θετικό αριθμό: "))

print("το παραγοντικό {}! είναι: {} ".format(n,paragontiko(n)))
print("τέλος προγράμματος")
