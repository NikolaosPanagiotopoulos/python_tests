#σε αυτό το παράδειγμα έχουμε λεξικά
#συγκρίνουμε τιμές και μετά εμφανίζονται τα αποτελέσματα
# Τα δεδομένα είναι οι πρωτεύουσες κρατών της Ευρωπαϊκής Ένωσης
#δημιουργούμε ενα λεξικό
#με κλειδιά τα κράτη και τιμές τις πρωτεύουσες από τις χώρες της Ευρώπης    
eu={"Αυστρία" : "Βιέννη",
"Βέλγιο" : "Βρυξέλλες",
"Βουλγαρία" : "Σόφια",
"Κροατία" : "Ζάγκρεμπ",
"Κύπρος" : "Λευκωσία",
"Τσεχία" : "Πράγα",
"Δανία" : "Κοπεγχάγη",
"Εσθονία" : "Τάλιν",
"Φινλανδία" : "Ελσίνκι",
"Γαλλία" : "Παρίσι",
"Γερμανία" : "Βερολίνο",
"Ελλάδα" : "Αθήνα",
"Ουγγαρία" : "Βουδαπέστη",
"Ιρλανδία" : "Δουβλίνο",
"Ιταλία" : "Ρώμη",
"Λετονία" : "Ρίγα",
"Λιθουανία" : "Βίλνιους",
"Λουξεμβούργο" : "Λουξεμβούργο",
"Μάλτα" : "Βαλέτα",
"Ολλανδία" : "Άμστερνταμ",
"Πολωνία" : "Βαρσοβία",
"Πορτογαλία" : "Λισαβόνα",
"Ρουμανία" : "Βουκουρέστι",
"Σλοβακία" : "Μπρατισλάβα",
"Σλοβενία" : "Λιουμπλιάνα",
"Ισπανία" : "Μαδρίτη",
"Σουηδία" : "Στοκχόλμη"}
#Δημιουργία αντιγράφου λεξικού για να γίνεται έλεγχος στοιχείων που λείπουν
eu_all=eu.copy()
print("Μαντέψτε τα κράτη της Ευρώπης και τις πρωτεύουσες τους")
#Δημιουργία endless loop
while True:
    #Αν τα βρει όλα το παιχνίδι τελειώνει
    if len(eu)==0:
        print("Τα βρήκες όλα. τελειωνει το παιχνίδι")
        break
    kratos=input("Πληκτρολογήστε ένα κράτος της ΕΕ ή q για έξοδο: ")
    #Σε περίπτωση που ο χρήστης ζητήσει έξοδο
    if kratos=="q":
        break  
    #Έλεγχος για το αν το κράτος υπάρχει
    if kratos in eu:
          #Αν το κράτος υπάρχει, ζητάμε την πρωτεύουσα
        prοteuousa=input("Πληκτρολογήστε την πρωτεύουσα του κράτους: ")
        if eu[kratos]==prοteuousa:
            #διαγραφή του στοιχείου από το λεξικό
            eu.pop(kratos)
            print("Μπράβο σωστά μάντεψες - Απέμειναν ακόμη {} κράτη να βρεις ".format(len(eu)))
        else:
            print("Δεν βρήκες την πρωτεύουσα-ξαναπροσπάθησε\n")
    else:
        if kratos in eu_all:
            print("Έχεις μαντέψει ήδη το κράτος αυτό")
        else:("δεν εδωσες σωστό κράτος, ξαναπρσπάθησε")

if len(eu)>0:
    print("\nΠλήρης λίστα\nΚράτος-Πρωτεύουσα")
    #Εμφάνιση ολων των σωστών απαντήσεων
    for k in eu_all.keys():
        print(k,"-",eu_all[k])
       