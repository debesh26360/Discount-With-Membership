total=0
a=input('enter yes or no for membership: ')
if a in ['y','yes','Yes','YES']:
    n=int(input('enter number of items: '))
    for i in range(n):
        cost=int(input('Please enter a item cost:'))
        total+=cost
    if total>=1000:
        print('Discount of 10%')
        total*=0.9
        print('final total is',total)
    elif total<1000:
        print('Discount of 5%')
        total*=0.95
        print('final total is',total)
elif a in ['n','no','No','NO']:
    n=int(input('enter number of items: '))
    for i in range(n):
        cost=int(input('Please enter a item cost:'))
        total+=cost
    if total>=1000:
        print('Discount of 5%')
        total*=0.9
        print('final total is',total)
    elif total<1000:
        print('No discount')
        total*=0.95
        print('final total is',total)
else:
    print('error')
