#even-odd 
n = int(input('enter number:'))

#simple if-else
#no need to use '(' ir ')'
if n%2 == 0:
    print('Even!!')
else:
    print('Odd!!')

#elif ladder

n = int(input('enter the amount of money you have:'))

#demonstration of 'and' operator
#similarly, 'or' can also be used where it is needed
if n>10000:
    print('you\'re damn rich!')
elif n<100000 and n>10000:
    #similar to else-if in c/c++
    print('you are doing just okay!')
elif n<10000 and n>1000:
    print('you need to work hard!')
else:
    print('Real enjoyment of life lies in struggle, my friend!')
