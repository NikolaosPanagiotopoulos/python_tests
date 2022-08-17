#σε αυτό το παράδειγμα θα δημιουργήσουμε συνάρτηση
#με 3 ορίσματα
#που θα υπολογίζει τις ηλικίες 5 ανθρώπων
#και θα τις εμφανίσουμε
def func_with_args(etos,onoma,fylo):
    if fylo=="γυναίκα":
        hlikia=2022-etos
        print("H κα {} είναι {} ετών. \n".format(onoma,hlikia))
    elif fylo=="άνδρας":
        hlikia=2022-etos
        print("Ο κος {} είναι {} ετών. \n".format(onoma,hlikia))
    else:
        hlikia=2022-etos
        print("Γεια σου {}. Είσαι {} ετών".format(onoma,hlikia))
    return "Δώστε τα στοιχεία του επόμενου ατόμου"
for i in range(5):
    name=input('Δώστε το όνομα του ατόμου: ')
    year=int(input('Δώστε ημερομηνία γέννησης του ατόμου: '))
    fy=input('Δώστε το φύλο του ατόμου: ')
    message=func_with_args(year,name,fy)
    print(message) if i!=4 else print('Τέλος εκτέλεσης.')
