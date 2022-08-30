#Σε αυτό το παράδειγμα θα χρησιμοποιήσουμε json
#θα μετατρέψουμε  αντικείμενα Pyhthon λεξικό ,λίστα,πλειάδα
#σε ένα JSON αντικείμενο (συμβολοσειρά) 
#με τη συνάρτηση  json.dumps()
import json
my_dict={'name':"Nick",'age':25}
print(my_dict)
print(type(my_dict))
my_dict_json=json.dumps(my_dict)
print(my_dict_json)
print(type(my_dict_json))
print("---------------------")
my_list=["White","Black",2]
print(my_list)
print(type(my_list))
my_list_json=json.dumps(my_list)
print(my_list_json)
print(type(my_list_json))
print("----------------------")
my_tuple=("Nick",25)
print(my_tuple)
print(type(my_tuple))
my_tuple_json=json.dumps(my_tuple)
print(my_tuple_json)
print(type(my_tuple_json))
print("------------------------")
my_float=15.01
print(my_float)
print(type(my_float))
my_float_json=json.dumps(my_float)
print(my_float_json)
print(type(my_float_json))
print("--------------------------")

