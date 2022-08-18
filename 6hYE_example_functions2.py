#σε αυτό το παράδειγμα θα δημιουργήσουμε συναρτήσεις
#θα δείχνουν πως λειτουργει ενα ατμ
#βασικές λειτουργίες
#1 Αρχικό μενου στοιχεία τράπεζας
#2 Έλεγχος pin
#3 Κεντρικό μενού χρήστη
#4 ανάληψη
#5 κατάθεση
#6 υπόλοιπο
#7 ακύρωση
#Συνάρτηση Αρχικό μενού
def start_menu():
    print("----Γεια σας---- αυτό είναι το ατμ της τράπεζας μας----")
    if  log_in():
        #print(f'Γεια σας κ {user["lastname"]} ')
        main_menu()
#δημιουργούμε ένα λεξικό για να αποθηκευσουμε τα στοιχεία χρήστη
user={
    'lastname': 'Monty',
    'pin':1234,
    'balance':5000
    }
#έλεγχος εγκυρότητας PIN
def check_pin(pin):
    if pin==user['pin']:
        return True
    else:
        return False
#Συνάρτηση που περιορίζει το PIN σε 3 προσπάθειες και μετά κλειδώνει
def log_in():
    tries=0
    while tries <3:
        pin=int(input("Πληκτρολογήστε τον κωδικό PIN: "))
        if check_pin(pin):
            print("PIN ok")
            return True
        else:
            print("λάθος PIN")
            tries+=1
    print("Οι 3 προσπάθειες έληξαν")
    print("Κλειδώθηκε η κάρτα σας από λάθος PIN")
    return False
#Συνάρτηση που δημιουργεί ένα κεντρικό μενού
def main_menu():
    print(f"Γεια σας κ {user['lastname']} ")
    print("\nΕπιλέξτε μία από τις παρακάτω επιλογές:")
    print("""\t1. ανάληψη\n \t2. κατάθεση\n \t3. υπόλοιπο\n \t4. ακύρωση\n """)
    query=int(input("\n Επιλέξτε εναν αριθμό από τις διαθέσιμες επιλογές: "))
    if query==1:
        print("Συνάρτηση για την ανάληψη")
        withdraw()
    elif query==2:
        print('Συνάρτηση για την κατάθεση')
        deposit()
    elif query==3:
        print('Συνάρτηση για το υπόλοιπο')
        balance()
    elif query==4:
        print('Συνάρτηση για την ακύρωση')
        print("\nΑκύρωση Συναλλαγής---\n Παρακαλούμε να παραλάβετε την κάρτα σας")
    else:
        print("Λάθος επιλογή. Δοκιμάστε ξανά \n")
#συνάρτηση εγκυρότητας ποσού
def validate_amount(amount):
    if amount<=user['balance']:
        return True
#συνάρτηση ανάληψης
def withdraw():
    while True:
        amount=int(input("\n Πληκτρολογήστε το ποσό προς ανάληψη: "))
        #Έλεγχος εγκυρότητας ποσού
        if validate_amount(amount):
            user['balance']=user['balance']-amount
            print(f"\n πραγματοποιήθηκε ανάληψη του ποσού {amount} € με επιτυχία.")
            print(f"\n το νέο υπόλοιπο είναι: {user['balance']}€")
            print('')
            break
        else:
            print(f"Το υπόλοιπο σας: {user['balance']}€ δεν επαρκεί είναι μικρότερο από: {amount}€ ")
            print(f"Η διαφορά είναι: {amount-user['balance']}€")
#συνάρτηση κατάθεσης
def deposit():
    while True:
        amount=int(input("\n Πληκτρολογήστε το ποσό προς κατάθεση: "))
        #ελεγχος εγκυρότητας ποσού
        if amount>0:
            user["balance"]=user["balance"]+amount
            print(f'\n Η κατάθεση του ποσού {amount}€ έγινε με επιτυχία')
            print(f'\n Το νέο σας υπόλοιπο είναι {user["balance"]}€')
            print(' ')
            break
        else:
            print("Το ποσό που έδωσες είναι λάθος. Προσπάθησε ξανά")
#συνάρτηση υπολοίπου, απλώς εμφανίζει το τρέχον ποσό
def balance():
    print(f"Το τρέχον υπόλοιπο ειναι: {user['balance']}€\n")
            
start_menu()




