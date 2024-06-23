x=int(input("Enter number :"))
while True:
    y=str(x)[::-1]
    x=x+int(y)
    if str(x) == str(x)[::-1]:
        print(x)
        break