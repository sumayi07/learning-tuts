# Day 3
age = 18
height = 177.8
cmplx = 2 + 1j

#triangle
base = (float)(input("Enter base: "))
height = (float)(input("Enter height: "))
print("The area of the triangle is ", base * height * 0.5)

side_a = (float)(input("Enter side a: "))
side_b = (float)(input("Enter side b: "))
side_c = (float)(input("Enter side c: "))
print("The perimeter of the triangle is ", side_a + side_b + side_c)

#rectangle
length = (float)(input("Enter length: "))
width = (float)(input("Enter width: "))
print("Area of rectangle is ", length * width)

#circle
radius = (float)(input("Enter radius: "))
print("Area of circle is ", 3.14 * radius ** 2)

# y = 2x -2
m = 2
x_intercept = 1
y_intercept = -2
print("Slope is ", m)
print("x intercept is ", x_intercept)
print("y intercept is ", y_intercept)

#other slope
m2 = (10 - 2)/(6 - 2)
distance = ((10 - 2)**2 + (6 - 2)**2)**0.5
print("Slope is ", m2)
print("Distance is ", distance)

#compare slopes
print("m1 is less than m2: ", m < m2)

#dragon and python
dlen = len("dragon")
plen = len("python")
print(dlen)
print(plen)
print(dlen < plen)

#and
print("on" in "python" and "on" in "dragon")

#in
print("jargon" in "I hope this course is not full of jargon.")

#convert
plen = float(plen)
plen = str(plen)

# if x % 2 == 0

#checks
print(7 // 3 == int(2.7))
print(type("10") == type(10))
print(int(9.8) == 10)

#table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")