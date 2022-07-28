try:
    a=int(input("Δώσε 1ο αριθμό"))
    b=int(input("Δώσε 2ο αριθμό"))
    result=a//b
except ZeroDivisionError:
    print("Εξαίρεση διαίρεση δια 0")
else:
    print(f"apotelesma {result}")
finally:
    print('OK')
#-------------------------
