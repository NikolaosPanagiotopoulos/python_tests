#σε αυτό το παράδειγμα θα χρησιμοποιήσουμε το εμφωλευμένο for
#θα εμφαανίζεται η προπαίδεια
#εξωτερική δομή επανάληψης
#το i λαμβάνει τιμές από 1 ως 10
for i in range(1,11):
    print("Προπαίδεια του ",i)
    #εμφωλευμένη δομή επανάληψης
    #το j λαμβάνει τιμές από 1 ως 10
    for j in range(1,11):
        print(i," επί ",j," = ",i*j)
    print("\n")
    
