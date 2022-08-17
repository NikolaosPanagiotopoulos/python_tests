#σε αυτό το παράδειγμα θα δημιουργήσουμε λεξικά        
#Θα διαγράψουμε στοιχεία με το del
print("----Πρώτο Λεξικό---")
students = {
    "names":["Άννα","Γιώργος","Βασιλική","Δημήτρης"],
    "age":[10,13,34,56]
    }
print('Εμφανίζουμε τα στοιχεία του λεξικού:')
for x in students.items():
    print(x)
print('\n')
del students['names']
print('Εμφανίζουμε τα στοιχεία του λεξικού μετά την διαγραφή με del')
for x in students.items():
    print(x)
print('\n')    
