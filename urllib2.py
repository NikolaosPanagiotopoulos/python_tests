#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε urillib.requests
#Με τη συνάρτηση urllib.request.urlopen() θα στείλουμε μία αίτηση 
#HTTP GET σε μία URL στο διαδίκτυο.
#θα χρησιμοποιήσουμε with ώστε να κλεινει μόνη της η συνδεση HTTP
#Θα βρούμε την κωδικοποίηση μέσω της ιδιότητας headers
import urllib.request
with urllib.request.urlopen("https://www.wikipedia.com/robots.txt") as f:
    message=f.read()
encoding=f.headers.get_content_charset()
print(encoding)
decoded_message=message.decode(encoding)
with open("my_file.txt",encoding='utf-8',mode='w') as my_file:
          my_file.write(decoded_message)

