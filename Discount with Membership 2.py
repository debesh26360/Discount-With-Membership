total=0
a=input('enter yes or no for membership')
if a in ['y','yes','Yes','YES']:
    n=int(input('enter number of items: '))
    for i in range(n):
        cost=int(input('Please enter a item cost:'))
        if cost>=1000:    
            print('You have won a discount by 15 percent')
            cost*=0.85
            total+=cost
            print('new cost is ', cost)
        elif cost<1000:
            print('You have won a discount by 5 percent')
            cost*=0.95
            total+=cost
            print('new cost is ', cost)
               
    print ('Now the total cost is ',total)

elif a in ['n','no','No','NO']:
    n=int(input('enter number of items: '))
    for i in range(n):
        cost=int(input('Please enter a item cost:'))
        if cost>=1000:    
            print('You have won a discount by 5 percent')
            cost*=0.85
            total+=cost
            print('new cost is ', cost)
        elif cost<1000:
            print('No discount')
            cost*=1
            total+=cost
            print('new cost is ', cost)
               
    print ('Now the total cost is ',total)
    
else:
    print('invalid option')





