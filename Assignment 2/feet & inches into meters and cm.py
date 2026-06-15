ft = float(input("Enter feet: "))
inch = float(input("Enter inches: "))

total_inches = (ft * 12) + inch
cm = total_inches * 2.54
m = cm / 100

print("Meters =", m)
print("Centimeters =", cm)