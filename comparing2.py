#σε αυτό το παράδειγμα έχουμε διάφορες δομές και συγκρίνουμε τιμές μεταξύ τους
#και μετά εμφανίζονται τα αποτελέσματα
#θα χρησιμοποιήσουμε μία βοηθητική λίστα
#για να μην εμφανίζονται πολλές φορές τα ιδια νούμερα
#θα χρησιμοποιήσουμε την sort() ώστε να εμφανίζονται ταξινομημένα τα νούμερα
paragelies = "4,4,4,5,2,3,8,6,3,2,5,1,5,9,8,6,5,2,9,10,10,2,4,2,2,5,4,4,4,5,5,1,4,10,9,10,5,10,9,4,6,7,4,4,10,4,6,10,7,5,5,9,8,7,9,7,7,1,1,4,8,9,8,6,4,7,8,3,10,5,10,9,8,1,8,5,6,4,4,9,9,1,4,5,8,3,9,5,10,3,2,4,5,7,10,7,3,6,3,7,9,8,4,10,8,10,1,2,5,6,8,10,5,3,4,2,3,1,2,8,9,1,9,9,3,7,2,2,3,1,3,4,6,9,8,4,9,2,10,1,9,2,3,3,9,3,2,1,8,1,8,7,5,10,7,5,3,4,4,3,7,7,2,5,4,7,6,7,5,5,3,5"

#το μετατρέπω σε λίστα
paragelies_list_s=paragelies.split(",")
#Η παραπάνω λίστα paragelies_list_s εχει τα ψηφία ως string
#Με επανάληψη for θα τα μετατρέψουμε σε αριθμούς και θα τα αποθηκεύσουμε
#σε μία νέα λίστα paragelies_list
paragelies_list=[]
for j in paragelies_list_s:
    paragelies_list.append(int(j))
paragelies_list.sort()
temp_list=[]
print(paragelies_list)
for i in paragelies_list:
    if i not in temp_list:
        freq=paragelies_list.count(i)
        temp_list.append(i)
        print("το προϊόν {} εχει παραγγελθεί {} φορές".format(i,freq))        

