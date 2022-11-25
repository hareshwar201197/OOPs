class shape():
    def area_of_triangle(self):
        Base = int(input("Enter  the base value :"))
        hight = int(input("Enter the hight value :"))
        formula = (1/2 * Base * hight)
        print("Area of triangle is :",formula)
        
    def square(self):
        side = int(input("Enter  the value side of triangle :"))
        formula = (side * side)
        print("Area of square is :",formula)

    def Circle(self):
        radius = int(input("Enter  the radius of circle :"))
        pi = 3.14
        formula = ( pi * radius * radius)
        print("Area of Circle  :",formula)


class_obj=shape()

# class_obj.area_of_triangle()

# class_obj.square()

class_obj.Circle()