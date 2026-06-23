EARTH_CIRCUMFERENCE = 24901
PI = 3.14159

radius = input("How many miles is the radius of your planet? ")

# Circumference = 2πr
c = 2 * PI * float(radius)

print("Your planet's circumference is", c)
if c > EARTH_CIRCUMFERENCE:
	print("That's bigger than planet Earth!")
