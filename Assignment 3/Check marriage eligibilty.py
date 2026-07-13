gender = input("Enter your gender (M/F): ").upper()
age = int(input("Enter your age: "))
if (gender == 'M' and age >= 21) or (gender == 'F' and age >= 18):
    print("You are eligible for marriage.")
else:
    print("You are not eligible for marriage.")