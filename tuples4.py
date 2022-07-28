#σε αυτό το παράδειγμα θα έχουμε πρόσβαση στα στοιχεία μιας πλειάδας
# επειδή οι πλειάδες ειναι αμετάβλητες
#πρώτα θα μετατρέψουμε την πλειάδα σε μία λίστα
#και θα κάνουμε αλλαγές στη λίστα
#και μετά θα κάνουμε μετρτοπή λίστας σε πλειάδα
print("=====Αρχική Πλειάδα========")
mytuple=('Python',5,'Μήλο',9.3,'Μπανάνα')
print(mytuple)
print('Τύπος:',type(mytuple))
print()
print("----------Μετατροπή σε Λίστα------------")
my_list=list(mytuple)
print(my_list)
print('Τύπος:',type(my_list))
print('-------ανάθεση νέας τιμής--------------')
my_list[1]='Γιώργος'
print(my_list)
print("Τύπος: ",type(my_list))
print()
print('=====Προσθήκη νέου στοιχείου============')
my_list.append('Σεμινάριο')
print(my_list)
print("Tύπος: ",type(my_list))
print()
print("---------μετατροπή σε πλειάδα------------")
mytuple=tuple(my_list)
print(mytuple)
print('Τύπος: ',type(mytuple))
print()
print('==========Προσθήκη Πλειάδας σε Πλειάδα============')
x=('Ελέφαντας',)
print('Πλειάδα 1: ',mytuple)
print('Πλειάδα 2¨: ',x)
mytuple+=x
print('Αθροισμα των πλειάδων ',mytuple)
print('Τύπος: ',type(mytuple))
print('=============Ένωση Πλειάδων===================')
mytuple2=('Πίτσα','Μπίρα','Μπάλα')
print('Πλειάδα 1: ',mytuple)
print('Πλειάδα 2: ',mytuple2)
mytuple3=mytuple+mytuple2
print('Αθροισμα πλειάδων ',mytuple3)
print('==============Πολλαπλασιαμός πλειάδας με αριθμό==============')
print('Πλειάδα2: ',mytuple2)
print('Πολλαπλασιάζω με τον αριθμό 3')
print('Αποτέλεσμα', mytuple2*3)

