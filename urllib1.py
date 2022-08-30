#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε urillib.requests
#Με τη συνάρτηση urllib.request.urlopen() θα στείλουμε μία αίτηση 
#HTTP GET σε μία URL στο διαδίκτυο.
#θα χρησιμοποιήσουμε with ώστε να κλεινει μόνη της η συνδεση HTTP
import urllib.request
with urllib.request.urlopen("https://www.wikipedia.com") as f:
    message=f.read()
decoded_message=message.decode('utf-8')
print('Μέρος του μηνύματος που λάβαμε από τον εξυπηρετητή: ')
print(message[0:101])
print('\n')
print("Ο τύπος του μηνύματος είναι: ",type(message))
print('\n')
print("Το μέρος του μηνύματος αποκωδικοποιημένο:")
print(decoded_message[0:101])
print('είναι τύπου: ',type(decoded_message))




