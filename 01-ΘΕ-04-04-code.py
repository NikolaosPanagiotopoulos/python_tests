####### 01-ΘΕ-04-04 Παράδειγμα 1 #######
mystr = "python"
print("First character: "+mystr[0])
print("String length: "+str(len(mystr)))
print("Last character: "+mystr[len(mystr)-1])

####### 01-ΘΕ-04-04 Παράδειγμα 2 #######
mystr = "python"
#1.	Ξεκίνα από τον τελευταίο χαρακτήρα και εκτύπωσέ τον.
print(mystr[len(mystr)-1])

#2.	Πήγαινε στον αμέσως προηγούμενο χαρακτήρα.

# φτιαχνουμε μια μεταβλητή για να κρατάμε τη θέση
# ξεκινάμε με την προτελευταία θέση
position = len(mystr)-2

#3.	Αν ο χαρακτήρας στον οποίο πήγαμε δεν είναι ο πρώτος χαρακτήρας της συμβολοσειράς, τότε:
#   3.1.	Εκτύπωσε τον χαρακτήρα
#   3.2.	Επανέλαβε τη διαδικασία από το βήμα 2
while (position!=0):
    #εκτύπωσε το χαρακτήρα στην τρέχουσα θέση
    print(mystr[position])
    #απομείωσε την τρέχουσα θέση κατά 1
    position = position -1

#4.	Αλλιώς αν είναι ο πρώτος χαρακτήρας τότε:
#   4.1.	Εκτύπωσε τον χαρακτήρα
print (mystr[position])

#5.	Τερμάτισε την εκτέλεση.

####### 01-ΘΕ-04-04 Παράδειγμα 3 #######
mystr = "python"
# μεταβλητή αποθήκευσης αποτελέσματος
revstr = ""

revstr += mystr[len(mystr)-1]
position = len(mystr)-2

while (position!=0):
    revstr += mystr[position]
    position = position -1

revstr += mystr[position]
print (revstr)

####### 01-ΘΕ-04-04 Παράδειγμα 4 #######
mystr = "python"
revstr = ""

position = len(mystr)-1

while (position!=-1):
    revstr += mystr[position]
    position = position -1

print (revstr)

####### 01-ΘΕ-04-04 Παράδειγμα 5 #######
for i in range(3, 10, 2):
    print(str(i))

####### 01-ΘΕ-04-04 Παράδειγμα 6 #######
for i in range(10, 3, -2):
    print(str(i))

####### 01-ΘΕ-04-04 Παράδειγμα 7 #######
mystr = "python"
revstr = ""

for i in range(len(mystr)-1, -1, -1):
    revstr += mystr[i]

print (revstr)

####### 01-ΘΕ-04-04 Παράδειγμα 8 #######
mystr = "serres"
revstr = ""

for i in range(len(mystr)-1, -1, -1):
    revstr += mystr[i]

if mystr == revstr:
    print ('Palindrome!')
else:
    print ('Non-palindrome')

####### 01-ΘΕ-04-04 Παράδειγμα 9 #######
mystr = input("Please enter some text: ")
revstr = ""

for i in range(len(mystr)-1, -1, -1):
    revstr += mystr[i]

if mystr == revstr:
    print ('Palindrome!')
else:
    print ('Non-palindrome')

####### 01-ΘΕ-04-04 Παράδειγμα 10 #######
mystr = input("Please enter some text: ")
mystr = mystr.lower()
mystr = mystr.replace(" ","")
revstr = ""


for i in range(len(mystr)-1, -1, -1):
    revstr += mystr[i]

if mystr == revstr:
    print ('Palindrome!')
else:
    print ('Non-palindrome')

####### 01-ΘΕ-04-04 Παράδειγμα 11 #######
import sys

mystr = input("Please enter some text: ")
mystr = mystr.lower()
mystr = mystr.replace(" ","")
revstr = ""


for i in range(len(mystr)-1, -1, -1):
    revstr += mystr[i]

if mystr == revstr:
    print ('Palindrome!')
else:
    print ('Non-palindrome')
print("user input = {} bytes".format(sys.getsizeof(mystr)))
print("reverse input = {} bytes".format(sys.getsizeof(revstr)))
print("counter i = {} bytes".format(sys.getsizeof(i)))

####### 01-ΘΕ-04-04 Παράδειγμα 12 #######
import sys

mystr = input("Please enter some text: ")
mystr = mystr.lower()
mystr = mystr.replace(" ","")

# θεωρώ ότι είναι παλίνδρομο μέχρι να εντοπίσω
# αποδείξεις ότι δεν είναι
palindrome = True

# μετρητές θέσεων
i=0 #από την 1η θέση
j=len(mystr)-1 #από την τελευταία θέση

# επανέλαβε όσο ο 1ος μετρητής είναι < του 2ου
while(i<j):
    # αν οι χαρακτήρες ΔΕΝ είναι ίδιοι, τότε
    if mystr[i]!=mystr[j]:
        # δεν έχουμε παλίνδρομο
        palindrome = False
        # σταμάτα την εκτέλεση των επαναλήψεων!
        break
    # στο τέλος κάθε επανάληψης, άλλαξε τους μετρητές
    i+=1 # αύξησε κατά 1 θέση
    j-=1 # μείωσε κατά 1 θέση

# ανάλογα με το αποτέλεσμα, δώσε την κατάλληλη έξοδο!
if palindrome:
    print('Palindrome!')
else:
    print ('Non-palindrome')

print("user input = {} bytes".format(sys.getsizeof(mystr)))
print("counter i = {} bytes".format(sys.getsizeof(i)))
print("counter j = {} bytes".format(sys.getsizeof(j)))
print("boolean result = {} bytes".format(sys.getsizeof(palindrome)))

####### 01-ΘΕ-04-04 Παράδειγμα 13 #######
import sys

mystr = input("Please enter some text: ")
mystr = mystr.lower()
mystr = mystr.replace(" ","")

# θεωρώ ότι είναι παλίνδρομο μέχρι να εντοπίσω
# αποδείξεις ότι δεν είναι
palindrome = True

# μετρητές θέσεων
i=0 #από την 1η θέση

# επανέλαβε όσο ο 1ος μετρητής είναι < του 2ου
while(i<len(mystr)-1-i):
    # αν οι χαρακτήρες ΔΕΝ είναι ίδιοι, τότε
    if mystr[i]!=mystr[len(mystr)-1-i]:
        # δεν έχουμε παλίνδρομο
        palindrome = False
        # σταμάτα την εκτέλεση των επαναλήψεων!
        break
    # στο τέλος κάθε επανάληψης, άλλαξε τους μετρητές
    i+=1 # αύξησε κατά 1 θέση


#for i in range(len(mystr)):
#    if mystr[i]!=mystr[len(mystr)-1-i]:
#        palindrome = False
#        break

if palindrome:
    print('Palindrome!')
else:
    print ('Non-palindrome')


print("user input = {} bytes".format(sys.getsizeof(mystr)))
print("counter i = {} bytes".format(sys.getsizeof(i)))
print("boolean result = {} bytes".format(sys.getsizeof(palindrome)))
