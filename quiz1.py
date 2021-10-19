# Nolan Piselli 10/19/21
# //
x = int(input("Enter the year of the date: "))
m = int(input("Enter the month of the date: "))
q = int(input("Enter the day of the date: "))
j = (x // 100)
k = (x % 100)

a = 26 * (m + 1) // 10
b = a + q
c = (k // 4) + (j // 4)
d = k + c
e = b + d + (5 * j)
h = e % 7

if h = 0:
    print("Saturday")
elif h = 1:
    print("Sunday")
elif h = 2:
    print("Monday")
elif h = 3:
    print("Tuesday")
elif h = 4:
    print("Wendsay")
elif h = 5:
    print("Thursday")
elif h = 6:
    print()