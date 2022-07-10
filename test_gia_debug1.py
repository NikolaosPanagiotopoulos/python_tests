#Σε αυτό το πρόγραμμα θα βάλουμε σκόπιμα ένα λάθος για να χρησιμοποιήσουμε το debugger
message="Καλημέρα"
new_message="_"
for i in range(len(message)):
    new_message+=message[i]+"_"
print(new_message)
