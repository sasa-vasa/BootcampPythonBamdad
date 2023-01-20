first_point = input("pls enter coordination of first point: ").split()
second_point = input("pls enter coordination of second point: ").split()
x1, y1 = int(first_point[0]), int(first_point[1]) 
x2, y2 = int(second_point[0]), int(second_point[1]) 
d = ((x1-x2)**2 + (y1-y2)**2)**0.5
print("distance between the two points is:", d)