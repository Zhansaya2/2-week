a = int(input())
b = int(input())
A = int(input())
B = int(input())
C = int(input())
if a <= B and b <= C or a <= C and b <= B:
    print("YES")
elif A <= B and b <= C or A <= C and b <= B:
    print("YES")
elif a <= B and A <= C or a <= C and A <= B:
    print("YES")
else:
    print("NO")
