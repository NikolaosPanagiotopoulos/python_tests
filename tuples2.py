#σε αυτό το παράδειγμα θα έχουμε πρόσβαση στα στοιχεία μιας πλειάδας
mytuple1="Python",5,"Μήλο",9.3,"Μπανάνα"
print('Πλειάδα:',mytuple1)
print('Πλήθος:',len(mytuple1))
print('Τύπος: ',type(mytuple1))
print()
#indexing
print("1η Πλειάδα",mytuple1)
print()
print("----------INDEXING--------")
print('Πρώτο Στοιχείο: ',mytuple1[0])
print('Δεύτερο Στοιχείο: ',mytuple1[1])
print('Τελευταίο Στοιχείο: ',mytuple1[-1])
print('Προτελευταίο Στοιχείο:',mytuple1[-2])
print()
#slicing
mytuple2=(3,'Python',5,'Μήλο',9.3,'Μπανάνα',9,38,'Γιώργος','Ελέφαντας',4)
print('--------slicing--------')
print(mytuple2[1:4])
print(mytuple2[:5])
print(mytuple2[2:])
print(mytuple2[:-2])
print(mytuple2[-3:])
print(mytuple2[-5:-2])
print(mytuple2[0:8:2])
print(mytuple2[::3])
print()
