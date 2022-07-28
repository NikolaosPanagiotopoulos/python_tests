#σε αυτό το παράδειγμα θα δούμε τις δομές δεδομένων
#λίστα
myList=["cat","dog","bird","crocodile","cat"]
print(myList[2])
#Πλειάδα
myTuple=("cat","dog","bird","crocodile","cat")
print(myTuple[2])
#συνολο
mySet={"cat","dog","bird","crocodile","cat"}
print(mySet)
#Λεξικό
myDict={
    "pet1":"cat",
    "pet2":"dog",
    "pet3":"bird",
    "pet4":"cat",
    "pet5":"crocodile"
    }
print(myDict["pet4"])
list_empty=list()
string_txt='Python'
my_list=list(string_txt)
print('Κενή Λίστα: ',list_empty,"\t\t\t\t\t=>",'τύπος',type(list_empty))
print("Συμβολοσειρά",string_txt,"\t\t\t\t\t=>",'τύπος',type(string_txt))
print("Νέα Λίστα",my_list,"\t\t=>",'τύπος',type(my_list))

    
