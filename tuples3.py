#σε αυτό το παράδειγμα θα έχουμε πρόσβαση στα στοιχεία μιας πλειάδας
#με δομή if και for
mytuple1="Python","Μήλο","Μπανάνα","Γιώργος","Ελέφαντας"
print('Πλειάδα:',mytuple1,'\n')
print('Πλήθος:',len(mytuple1))
print('Τύπος: ',type(mytuple1))
print()
print("----------Έλεγχος ύπαρξης στοιχείου--------")
if 'Python' in mytuple1:
    print('Το στοιχείο "Python" υπάρχει στην πλειάδα.')    
print("---------Πρόσβαση Στοιχείων------------------")
for x in mytuple1:
    print('Στοιχείο:',x)
print()
print("---------Πρόσβαση Στοιχείων μέσω index------------------")
for i in range(len(mytuple1)):
    print(f'Στοιχείο με index {i}:',mytuple1[i])    
