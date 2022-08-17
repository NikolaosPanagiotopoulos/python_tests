#σε αυτό το παράδειγμα θα δημιουργήσουμε λεξικά        
#Θα χρησιμοποιήσουμε μία δομή επανάληψης
#για να διατρέξουμε ολα τα στοιχεία του λεξικού
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
print("--------εμφανιση των στοιχείων mydict.keys()-----")
i=1
for x in my_dict.keys():
    print("Το {}ο κλειδί είναι: {}".format(i,x))
    i+=1
print("--------εμφανιση των στοιχείων mydict.values()-----")
i=1
for x in my_dict.values():
    print("H {}η τιμή ειναι: {}".format(i,x))
    i+=1
print('\n')
    
