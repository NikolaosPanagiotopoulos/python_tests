#σε αυτό το παράδειγμα θα δημιουργήσουμε λεξικά        
#1ο λεξικό
print("----=====Πρώτο Λεξικό-----------==========-----")
myteam= {
    "name": ["Robert","Leon","Manuel","Steven"],
    "surname": ["Jameson","Walker","Carpender","Jones"],
    "numbers": [9,8,1,34]
}
print(myteam)
print("Το πλήθος των αντικειμένων του πρώτου λεξικού ειναι {} και ο τύπος ειναι {}".format(len(myteam),type(myteam)))
#2ο λεξικό
print("----=====--------Δεύτερο Λεξικό-----------==========-----")
fruit={
    "type": "Apple",
    "shape": "round",
    "color": "red",
    "quantity": 40
}
print("τα στοιχεία του δεύτερου λεξικού είναι ",fruit)
print("Το πλήθος των αντικειμένων του δεύτερου λεξικού ειναι {} και ο τύπος ειναι {}".format(len(fruit),type(fruit)))
#τρίτο λεξικό
print("----=====Τρίτο Λεξικό-----------==========-----")
fruit2= {
    "type":"Apple",
    "shape":"round",
    "color": ["red","green","yellow"],
    "quantity": [40,20,10],
    "isEdible": True
}
print("Το τρίτο λεξικό έχει τα στοιχεια ",fruit2)
print("Το πλήθος των αντικειμένων του τρίτου λεξικού ειναι {} και ο τύπος ειναι {}".format(len(fruit2),type(fruit2)))
#τέταρτο λεξικό
print("-----------τέταρτο λεξικό---------------")
d=dict(name=['Nick','Maria'], sex=["male","female"],age=46)
print("το τέταρτο λεξικό έχει τα στοιχεία ",d)
print("Το πλήθος των αντικειμένων του τέταρτου λεξικού ειναι {} και ο τύπος ειναι {}".format(len(d),type(d)))
