num=int(float(input("δώστε εναν αριθμό: ")))
while(num!=10):
    mod=num%2
    if mod>0:
        print("ο αριθμός",num,"είναι περιττός.")
    else:
        print("ο αριθμός",num,"είναι άρτιος.")
    num=int(float(input("δώστε εναν αριθμό: ")))
    
