#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 1
string ="In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. The latter may allow its elements to be mutated and the length changed, or it may be fixed (after creation). A string is generally considered as a data type and is often implemented as an array data structure of bytes (or words) that stores a sequence of elements, typically characters, using some character encoding. String may also denote more general arrays or other sequence (or list) data types and structures."
print(string)





#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 2
multi_string = """In computer programming, a string is traditionally 
a sequence of characters, either as a literal constant or as some kind
of variable. The latter may allow its elements to be mutated and the
length changed, or it may be fixed (after creation). A string is
generally considered as a data type and is often implemented as an array
data structure of bytes (or words) that stores a sequence of elements, 
typically characters, using some character encoding. String may also
denote more general arrays or other sequence (or list) data types and structures."""
print(multi_string)





#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 3
mystring = "strings are great fun"
print("strings")
print("are")
print("great")
print("fun")




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 4
mystring = "strings\nare\ngreat\nfun"
print(mystring)




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 5
mystring = "strings\rare\rgreat\rfun"
print(mystring)




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 6
#για 100 φορές, επανέλαβε τη διαδικασία:
# εκτύπωσε το τρέχον βήμα (0 - 99),
# επαναφέροντας μετά τον κέρσορα στην αρχή
# περίμενε 0.2 δευτερόλεπτα
import time
for i in range(100):
    print("Loading: "+str(i)+"%\r", end="")
    time.sleep(0.2)




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 7
heading = "Player Joined Games Wins"
player1 = "AA 2021 15 2"
player2 = "AB 2019 2 2"

print("\n")
print(heading)
print(player1)
print(player2)




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 8
heading = "Player\tJoined\tGames\tWins"
player1 = "AA\t2021\t15\t2"
player2 = "AB\t2019\t42\t34"

print("\n")
print(heading)
print(player1)
print(player2)

#### στη συνέχεια, ως μεταβλητή string νοείται αυτή που
#### δηλώσαμε στο παράδειγμα 1.




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 9
n_sent = string.count(".")
print(n_sent)




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 10
print(string.count("a"))
print(string.count("string"))




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 11
print(string.count("a")/len(string))




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 12
substring = string[0:64]
print(substring)
print(substring.count(" "))




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 13
badstring = " String with leading and training whitespace. "
print(badstring)
print(badstring.strip())
print(badstring.lstrip())
print(badstring.rstrip())




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 14
string2 = """ In computer programming, a string is traditionally 
a sequence of characters, either as a literal constant or as some kind 
of variable. The latter may allow its elements to be mutated and the 
length changed,  or it may be fixed (after creation). A string is 
generally considered as a data type and is often implemented as an array 
data structure of bytes (or words) that stores a sequence of elements, 
typically characters, using some character encoding. String may also 
denote more general arrays or other sequence (or list) data types and structures. """

print("word count before string cleansing")
print(string2.count(" "))
#1. αφαίρεση περιττών αρχικών και τελικών διαστημάτων
string2 = string2.strip()
#2. αντικατάσταση διπλών διαστημάτων
string2 = string2.replace("  ", " ")
#3. τελική καταμέτρηση
print("word count after string cleansing")
print(string2.count(" ")+1)





#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 15
string = "In computer programming, a string is traditionally a sequence of characters, either as a literal constant or as some kind of variable. The latter may allow its elements to be mutated and the length changed, or it may be fixed (after creation). A string is generally considered as a data type and is often implemented as an array data structure of bytes (or words) that stores a sequence of elements, typically characters, using some character encoding. String may also denote more general arrays or other sequence (or list) data types and structures."
print(string.replace(" ","\n"))





#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 16
#1. μετατροπή σε μικρά
processed_string = string.lower() 
#2.1 απαλοιφή κομμάτων και τελειών
processed_string = processed_string.replace(",","") 
processed_string = processed_string.replace(".","") 
#2.2 απαλοιφή παρενθέσεων
processed_string = processed_string.replace("(","") 
processed_string = processed_string.replace(")","")
#3. αντικατάσταση κενών με νέα γραμμή
processed_string = processed_string.replace(" ","\n") 
#4. εκτύπωση αποτελέσματος
print(processed_string)




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 17
name = "Jim"
surname = "Beam"
slogan = "This ain't "+name+" "+surname+"!"
print(slogan)





#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 18
name = "Jim"
surname = "Beam"
age = 23
print("This bottle of "+name+" "+surname+" is "+age" years old")




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 19
name = "Jim"
surname = "Beam"
age = 23
print("This bottle of "+name+" "+surname+" is "+str(age)+" years old")




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 20
#1. Ορισμός συμβολοσειράς - πρότυπο
outstr = "This bottle of {} {} is {} years old"
#2. Ορισμός τιμών μεταβλητών
name = "Jim"
surname = "Beam"
age = 23
#3. Εκτύπωση με πάραθεση των μεταβλητών στη σωστή σειρά
print(outstr.format(name, surname, age))




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 21
str = "Hello. This is a test. I repeat, a test. Bye now."
#ακριβές μέσο της συμβολοσειράς
print(len(str)/2)
#στρογγυλοποιημένο μέσο
print(int(len(str)/2))
#χαρακτήρας στο στρογγυλοποιημένο μέσο
#θυμηθείτε, η αρίθμηση είναι από το 0
#άρα αν το μέσο είναι ο n-οστός χαρακτήρας,
#η αντίστοιχη θέση είναι η n-1
print(str[int(len(str)/2)-1])




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 22
str = "Hello. This is a test. I repeat, a test. Bye now."
print(str[0:int(len(str)/2)])
print(str[int(len(str)/2):])




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 23
str = "Hello. This is a test. I repeat, a test. Bye now."
#ακριβές μέσο της συμβολοσειράς
midpoint = int(len(str)/2)
#τελευταία θέση του ". " ψάχνοντας από την αρχή
#μέχρι το ακριβές μέσο
target_pos = str.rfind(". ", 0, midpoint)
#Ας κόψουμε τώρα τη συμβολοσειρά, από την αρχή
#μέχρι το σημείο που τελείωνουν οι πρώτες μισές προτάσεις
print(str[0:target_pos+1])
#και τώρα το άλλο μισό
print(str[target_pos+2:])




#01-ΘΕ-03-ΥΕ-04 ΠΑΡΑΔΕΙΓΜΑ 24
str = input("Please enter some text")
#ακριβές μέσο της συμβολοσειράς
midpoint = int(len(str)/2)
#τελευταία θέση του ". " ψάχνοντας από την αρχή
#μέχρι το ακριβές μέσο
target_pos = str.rfind(". ", 0, midpoint)
#Ας κόψουμε τώρα τη συμβολοσειρά, από την αρχή
#μέχρι το σημείο που τελείωνουν οι πρώτες μισές προτάσεις
print(str[0:target_pos+1])
#και τώρα το άλλο μισό
print(str[target_pos+2:])

