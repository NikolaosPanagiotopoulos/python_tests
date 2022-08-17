#σε αυτό το παράδειγμα θα δημιουργήσουμε λεξικά        
#Θα χρησιμοποιήσουμε εμφωλευμένες δομές επανάληψης
#για να διατρέξουμε ολα τα στοιχεία του λεξικού
#που είναι μέσα σε λίστες
print("----Πρώτο Λεξικό---")
my_dict = {
    "name":["John","Jack","Jason","James"],
    "age":[23,24,67,4],
    "country": ["Greece","Germany","USA","Iceland"],
    "hair_color": ['blonde','brunette','black','auburn']
}
print(my_dict)
print("-----εμφάνιση των στοιχείων  print(x)------")
for x in my_dict:
    print(x)
print("-----εμφάνιση των στοιχείων print(my_dict[x])------")
for x in my_dict:
    print(my_dict[x])
print("--------εμφανιση των στοιχείων mydict.items()-----")
i=1
for x in my_dict.values():
    print("Η {}η τιμή είναι: {}".format(i,x))
    j=1
    for y in x:
        print("Το {}ο στοιχείο της λίστας της {}ης τιμής είναι: {}".format(j,i,y))
        j+=1
    i+=1
    print('\n')
    
