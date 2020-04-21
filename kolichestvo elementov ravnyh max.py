n = int(input())
max = n
len = 1
while n != 0:
    n = int(input())
    if n > max:
        max = n
        len = 1
    elif n == max:
        len += 1
print(len)
