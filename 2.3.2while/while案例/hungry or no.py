feel=input('hungry or no:')
n=1
if feel=='no':
    print('your are full')
else:
    while feel=='hungry':
        print('eat',n,'th rice')
        n=n+1
        feel1=input('hungry or no:')
        if feel1=='no':
            print('your are full final')
            break
