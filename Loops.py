students = ['Anu','anjali','anna','arya','alen']
for n in students:
    print(n)

#printing all names using for loop in sorted order
print('Sorted list of names')
students.sort()
for n in students:
    print(n)

#while loop
print('While Loop')
n = 0
while n < len(students) :
    print(students[n])
    n = n+1

