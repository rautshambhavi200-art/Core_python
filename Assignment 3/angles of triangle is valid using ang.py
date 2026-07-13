a = int(input("Enter the first angle of the triangle: "))
b = int(input("Enter the second angle of the triangle: "))
c = int(input("Enter the third angle of the triangle: "))

if a + b + c == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")