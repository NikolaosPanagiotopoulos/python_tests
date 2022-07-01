#01-ΘΕ-03-ΥΕ-01 - Παράδειγμα 1
message = """Αυτή είναι μια συμβολοσειρά
η οποία καταλαμβάνει
6 γραμμές.
Προσοχή ότι γίνεται χρήση τριπλών εισαγωγικών
και στην αρχή και στο τέλος
της συμβολοσειράς!"""

print (message)




#01-ΘΕ-03-ΥΕ-01 - Παράδειγμα 2
message1 = "Τιμοκατάλογος - \"Ιταλική Πιτσαρία\""
message2 = 'Τιμοκατάλογος - "Ιταλική Πιτσαρία"'

print (message1)
print (message2)




#01-ΘΕ-03-ΥΕ-01 - Παράδειγμα 3
message = "Καλημέρα!\nΣήμερα\t\tέχει λιακάδα.\nΕυκαιρία\tγια βόλτα!"
print(message)




#01-ΘΕ-03-ΥΕ-01 - Παράδειγμα 4
message = "Καλημέρα! Σήμερα έχει λιακάδα"

print (message)
print (message[0:4])
print (message[10:])
print (message[-7:])
print (message[0:8:2])




#01-ΘΕ-03-ΥΕ-01 - Παράδειγμα 5
message = "Καλημέρα! Σήμερα έχει λιακάδα"

print(message.upper())
print(message.lower())
print(message.replace("ε","Ω"))
print(message.count("α"))
print(message.isdigit())




#01-ΘΕ-03-ΥΕ-01 - Παράδειγμα 6
message = "Καλημέρα! Σήμερα έχει λιακάδα"
mikos = len(message)
print ("Η συμβολοσειρά έχει",mikos,"χαρακτήρες")