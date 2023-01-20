a = float(input("Pls enter 1st side: "))
b = float(input("Pls enter 2nd side: "))
c = float(input("Pls enter 3rd side: "))
p = (a+b+c)
s = (p/2*(p/2-a)*(p/2-b)*(p/2-c))**0.5
print("Perimeter of triangle is:", p, "\nArea of triangle is:", s)