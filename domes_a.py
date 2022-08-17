#σε αυτό το παράδειγμα θα δημιουργήσουμε διαφορετικές
#δομές και θα τις εμφανίσουμε

mylist = [5, "5", "test", "True"]
print(mylist)
mytuple = 5, "5", "test", "True"
print(mytuple)
list1=list(mytuple)
print(list1)
list1.insert(1,"Nikos")
print("list1",list1)
tuple1=tuple(list1)
print("tuple1",tuple1)
