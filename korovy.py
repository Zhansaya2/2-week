n = int(input())
if 10 < n < 20 or n % 10 != 1 and n % 10 != 2 and n % 10 != 3 and n % 10 != 4:
    print(n, 'korov')
else:
    if n % 10 == 1:
        print(n, 'korova')
    else:
        print(n, 'korovy')
