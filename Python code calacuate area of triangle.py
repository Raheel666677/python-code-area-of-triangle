Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... def calculate_triangle_area(base, height):
...     area = (base * height) / 2
...     return area
... base = float(input("Enter the base of the triangle: "))
... height = float(input("Enter the height of the triangle: "))
... area = calculate_triangle_area(base, height)
... print(f"The area of the triangle with base {base} and height {height} is: {area}")
