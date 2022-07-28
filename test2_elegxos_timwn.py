x=int(input('dvse enan arithmo: '))
if (x%2):
    a=5
    if x*a>=30:
        b=15
        c=20
    else:
        b=5
    c=10
    x=b//a+c*x
else:
    a=10
    if x*a>=30:
        b=30
        c=40
    else:
        b=20
    c=20
    x=b/a+c*x
print(x)
