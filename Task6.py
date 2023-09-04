import math

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):                          #for:pi*R2
        return math.pi * self.radius ** 2  #pi=3.14159

def main():
    while True:
        print("1. Calculate area of a square")
        print("2. Calculate area of a triangle")
        print("3. Calculate area of a circle")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "":
            print("Exiting the program.")
            break
        
        choice = int(choice)
        
        if choice == 1:
            side_length = float(input("Enter the side length of the square: "))
            square = Square(side_length)
            print(f"The area of the square is: {square.area()}")
        elif choice == 2:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            triangle = Triangle(base, height)
            print(f"The area of the triangle is: {triangle.area()}")
        elif choice == 3:
            radius = float(input("Enter the radius of the circle: "))
            circle = Circle(radius)
            print(f"The area of the circle is: {circle.area()}")
        elif choice == 4:
            print("Exiting the program.")
            break
        elif choice >= 4:
            print("Invalid choice. Please select a valid option.")
            

if __name__ == "__main__":
    main()
