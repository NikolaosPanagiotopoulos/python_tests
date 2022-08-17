#σε αυτό το παράδειγμα θα δημιουργήσουμε σύνολα sets
#Θα προσθέσουμε στοιχεία με update()
print("----Σύνολο1---")
print("-----------Θα δημιουργήσουμε ενα σύνολο με set()----------------- ")
myset1=set(("a","b","c","d","e","f","g"))
print(myset1)
my_list=[1,2,3,4]
print(my_list)
my_tuple=("Hello",10)
print(my_tuple)
myset1.update(my_list,my_tuple)
print(myset1)



