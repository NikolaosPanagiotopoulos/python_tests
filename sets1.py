#σε αυτό το παράδειγμα θα δημιουργήσουμε σύνολα sets
print("----Σύνολο1---")
myset = {"dog","cat","mouse"}
print(myset)
print("------Σύνολα 2 ως 4------")
int_set={1,2,3,4}
str_set={"John","Mary","Dean","Sam"}
mix_set={"Hello",True,"False",2.1,3}
print("Σύνολο ακεραίων ",int_set)
print("Σύνολο συμβολοσειρών ",str_set)
print("Σύνολο διαφορετικών τύπων δεδομένων ",mix_set)
print("-----------Σύνολo 5---------------")
#αν βάλουμε διπλές ίδιες τιμές τις αγνοεί και περιέχει
#μόνο μία φορά την κάθε τιμή
myset1={"This","set","contains","some","some","some","this","set","duplicates","duplicates"}
print (myset1)
print("-----------Θα δημιουργήσουμε ενα σύνολο με set()----------------- ")
myset2=set(("a","b","c","d","e","f","g"))
print(myset2)
print(len(myset2))
print(type(myset2))
print("-----------Θα έχουμε πρόσβαση στα στοιχεία του συνόλου δομή επανάληψης ----------------- ")
for x in myset2:
    print(x)
print("-----------Θα δούμε τα στοιχεία του συνόλου με in και not in----------------- ")
print(myset2)
print ("ανήκει στο σύνολο το \"g\" ; ","g" in myset2)
print("ανήκει στο σύνολο το 7 ; ",7 in myset2)
print("Δεν ανήκει στο σύνολο το 10  ",10 not in myset2)
print("Δεν ανήκει στο σύνολο το \"a\" ; ","a" not in myset2)




