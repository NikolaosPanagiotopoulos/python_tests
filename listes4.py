#σε αυτό το παράδειγμα θα έχουμε πρόσβαση στα στοιχεία της λίστας
#με διαφορετικούς τρόπους
my_list=['Python','Μήλο','Μπανάνα',"Γιώργος","Ελέφαντας","Μαρία","Μανώλης","Ραδιόφωνο"]
mikos=len(my_list)
print('λίστα',my_list)
print(f"το μήκος της λίστας είναι {mikos}")
print('Τύπος',type(my_list))
print('----έλεγχος ύπαρξης στοιχείου---------')
if 'Python' in my_list:
    print('Το στοιχείο "Python" υπάρχει στην λίστα.')
print()
print('-----Πρόσβαση στοιχείων----------------')
for x in my_list:
    print('Στοιχείο:',x)
print()
print("---------Πρόσβαση στοιχείων μέσω του index-----------")
for i in range(len(my_list)):
    print(f'Στοιχείο με index {i} :',my_list[i])
print()
print("--------Πρόσβαση στοιχείων με χρήση της while---------")
i1=0
while i1<len(my_list):
    print(f"Στοιχείο με index {i1}:",my_list[i1])
    i1=i1+1
