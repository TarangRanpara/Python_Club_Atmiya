#maths operators

n1 = int(input('enter num1:'))
n2 = int(input('enter num2:'))

print('addition:',n1+n2)
print('substraction:',n1-n2)
print('multiplication:',n1*n2)
print('division:',n1/n2)
print('division without decimal point:',n1//n2)
print('power:',n1**n2)

#string multiplication
s = input('enter string:')
n = int(input('how many times you want it to repeat:'))

#string multiplication
print(s*n)

#doing it legendary way!, only one variable
print(
    s*(int(input('\nhow wany times you want to repeat the string:')))
)

#doing it Ultra legendary way! No variables at all
print(
    (input('\nenter string:')) * ( int(input('how many times you want it to repeat:')) )
)