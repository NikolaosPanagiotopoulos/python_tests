#σε αυτό το παράδειγμα θα έχουμε λίστες μέσα σε λίστες
#με δύο δείκτες βρίσκουμε τα στοιχεία της εσωτερικής λίστας
list_a=['Python',3,'καλημέρα',['Γιώργος',1,True],'Πορτοκάλι']
mikosa=len(list_a)
print('list_a:',list_a,'\n')
print(f"το μήκος της λίστας a είναι {mikosa}",'\n')
print(list_a[3])
print(list_a[3][0])
print(list_a[3][1])
print(list_a[3][2])
list_a[3][0]='Πανεπιστήμιο'
list_a[3][1]='Πατρών'
print(list_a)
