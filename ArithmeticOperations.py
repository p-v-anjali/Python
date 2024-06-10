
a = int(input('Enter First number : '))#intentation(spacing) -global scope (starting with margin) 
b = int(input('Enter Second Number : '))
Op = input('Enter the operation  +,-,*,/ : ')

if Op == '+':
    print(a+b)   #result = a+b
elif Op == '-':
    print(a-b)   #result = a-b
elif Op == '*':
    print(a*b)   #result = a*b
elif Op == '/':
    if b==0:   
        print('Division by zero is not possible')
    print(a/b)  #result = a/b
                #print(result)

else:
    print('Invalid Operation')

