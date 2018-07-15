#python accepts input in the form of string only.
#you have to convert into relevent type accoringly

#bad practice
print('enter name:')
name = input()

print('name:',name)

#good practice
name = input('enter name:')
print('name:',name)



#if you want to accept a number

#way-1: bad practice
n = input('enter number:')
n = int(n)

print('number:',n)

#wat-2: good practice
n = int(input('enter number:'))

print('number:',n)



#there are other conversions too
n = float(input('enter float number:'))

print('number:',n)

#now you have n = 123.123 & you want to convert it into '123.123'
n = str(n)
print('number:',n)



#there's one 'Legendary' way to accept & print the number!!

print('number is:', int(input('enter number:') ))
