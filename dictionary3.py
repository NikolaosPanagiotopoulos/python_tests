#σε αυτό το παράδειγμα θα δημιουργήσουμε λεξικά        
#Θα έχουμε πρόσβαση στα στοιχεία του λεξικού με την μέθοδο items()
print("----Πρώτο Λεξικό---")
ucl_finalists= {
    "teams":["Βιγιαρεάλ","Ρεάλ Μαδρίτης","Μάντσεστερ Σίτυ","Λίβερουλ"],
    "country":["Ισπανία","Αγγλία"],
    "color": ["Κόκκινα","Πράσινα","Κίτρινα"],
    "final": 4
}
stoixeia=ucl_finalists.items()
print("Στοιχεία των φιναλίστ στο Champions League: ",stoixeia,'\n')
print("----Προσθήκη νέων στοιχείων---")
ucl_finalists['Knocked_out']=['Μπάγερν Μονάχου','Τσέλσι','Ατλέτικο Μαδρίτης','Μπενφίκα']
print('Ανανεωμένα στοιχεία των φιναλίστ στο Champions League: ',stoixeia)
