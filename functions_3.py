#σε αυτό το παράδειγμα θα δημιουργήσουμε μία συνάρτηση
#όπου θα δίνει ο χρήστης μία λίστα τιμών χωρισμένη με κόμματα
#και μετά η συνάρτηση θα εμφανίζει την ίδια λίστα
#αντιστραμμένη με τη μέθοδο reverse()
def antistrammeni_lista(my_list):
    my_list.reverse()
    return my_list
mylist=input("Πληκτρολογήστε μία ακολουθία τιμών χωρισμένες με κόμματα ")
mylist=list(mylist.split(","))
print("Η αρχική λίστα που έδωσες ήταν: {} ".format(mylist))
while(len(mylist)!=1):
    reverted=antistrammeni_lista(mylist)
    print("η αντιστραμμένη λίστα ειναι: {}".format(reverted))
    mylist=input("Πληκτρολογήστε μια ακολουθία τιμών χωρισμένη με κόμματα ")
    mylist=list(mylist.split(","))
    print("Η αρχική λίστα που έδωσες ειναι {}".format(mylist))
else:
    print("Τέλος εκτέλεσης του προγράμματος ")
    
