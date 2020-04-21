now = int(input())
while now != 0:
    s = int(input())
if s > now:
    a = now
    now = s
elif now > s > a:
    a = s
elif s == 0:
    now = s
print(a)
