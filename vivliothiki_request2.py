#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε import requests
#για να εχουμε πρόσβαση στο API του ΟΠΑΠ
#και θα ζητήσουμε τα αποτελέσματα της κλήρωσης Τζόκερ
#θέλουμε την συγκεκριμένη κλήρωση που έχει ID 5104
#θα στείλουμε αίτηση στο URL
#https://api.opap.gr/draws/v3.0/5104/last-result-and-active
#Θα χρησιμοποιήσουμε τη μέθοδο json() του Response αντικειμένου που
#θα δημιουργηθεί.
import requests
req=requests.get("https://api.opap.gr/draws/v3.0/5104/last-result-and-active")
print('Ο τύπος δεδομένων που επιστρέφεται από την μέθοδο json είναι: ',type(req.json()),'\n')
print('Ο τύπος δεδομένων που επιστρέφεται από την ιδιότητα text ειναι: ',type(req.text),'\n')
data=req.json()
print(data,'\n')
print("Τα κλειδιά του επιστρεφόμενου λεξικού είναι: ", data.keys(),"\n")
print("Τα κλειδιά του πρώτου εμφωλευμένου λεξικού είναι: ", data['last'].keys(),"\n")
print('Οι νικητήριοι αριθμοί της κλήρωσης είναι: ',data['last']['winningNumbers']['list'],'και τζόκερ το νούμερο',data['last']['winningNumbers']['bonus'][0],'.')


       
