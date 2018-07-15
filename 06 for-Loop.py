#it uses range() function about which youcan easily google!!

#don't forget ':' for start of block & one tab space for statements in block

#variation-1
#from 0 to 9, 10 is exclusive
for i in range(10):
    print('hello:',i)
    print('\n\n')


#variation-2
#explicitely giving lower limits
for i in range(0,10):
    print('hello:',i)
    print('\n\n')

#variation-3
#explicitely giving lower limits & increment value:2
for i in range(0,10,2):
    print(i)

#variation-4
#reverse order & decrement value:-2
for i in range(10,0,-2):
    print(i)

#doing it 'Legendary way'
for i in range(int(input('enter lower limits:')), int(input('enter higher limit:'))+1):
    print(i)




    






     