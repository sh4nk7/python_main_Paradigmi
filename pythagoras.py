''''
Pythagoras with Python
Which right triangle…
that has integers for all sides…
and all sides equal to or smaller than 10…
has a perimeter of 24?
Solve using a comprehension
''''

# List comprehension to generate all possible combinations of sides
triangles = [(a, b, c) for a in range(1, 11) for b in range(1, 11) for c in range(1, 11)
             if a + b + c == 24 and a ** 2 + b ** 2 == c ** 2]

# Print the triangles with perimeter 24
for triangle in triangles:
    print("Triangle with sides:", triangle)
