#σε αυτό το παράδειγμα θα διαγράψουμε στοιχεία μιας λίστας με διαφορετικούς τρόπους
list_a=['Python',5,'Μήλο','Μπανάνα','Πορτοκάλι']
list_b=["Γιώργος",2,"Ντομάτες",5,"Πατάτες",7,"Κρεμμύδια"]
mikosa=len(list_a)
mikosb=len(list_b)
print('list_a:',list_a,'\n')
print(f"το μήκος της λίστας a είναι {mikosa}",'\n')
del list_a[3]
del list_b[1:3]
print(list_a)
print(list_b)
