#σε αυτό το παράδειγμα θα αλλάξουμε τα στοιχεία μιας λίστας με for και τους τελεστές + = και *=
list_a=['Python',5,'Μήλο','Μπανάνα','Πορτοκάλι']
list_b=["Γιώργος"]
mikosa=len(list_a)
mikosb=len(list_b)
print('list_a:',list_a,'\n')
print(f"το μήκος της λίστας a είναι {mikosa}",'\n')
for x in range(1,4):
    print(f"επανάληψη {x} ")
    list_a+=['Python']
    print(list_a)
    list_b*=2
    print(list_b)
