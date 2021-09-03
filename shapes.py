def circle():

    radius = input("Enter the radius: ")


    pi = 3.14159

    cirle_area = pi * int(radius) ** 2

    print("Circle: ", "r =", radius, "area =", cirle_area)


def sphere():
    radius = input("Enter the radius: ")

    pi = 3.14159

    sphere_volume = 4/3 * pi * int(radius) ** 3

    print("Sphere: ", "r =", radius, "volume =", sphere_volume)

def rectangle():

    rc_height = input("Enter height of the rectangle: ")

    width = input("Enter width of the rectangle: ")

    rec_area = int(rc_height) * int(width)

    print("Rectangle: ", "Height =", rc_height, "Lenght", width, "area =", rec_area)

def square():
    
    sq_length = input("Enter length of the square: ")

    sq_area = int(sq_length) ** 2

    print("Square: ", "side length =", sq_length, "area =", sq_area)
 
def isosceles_triangle():

    base = input("Enter side length of the Isosceles triangle: ")

    t_height = input("Enter height of the triangle: ")

    area = ( int(base) **2 * int(t_height) ** 2) ** .5

    print("Isosceles Triangle: ", "side =", base, "height =", t_height, "area =", area)
    

def equilateral_triangle():

    et_length = input("Enter length of the equilateral triangle: ")

    area = ((3 ** .5) / 4) * int(et_length) ** 2

    print("Equilateral Triangle: ", "side =", et_length, "area =", area)

def trapezoid():


    t1_base = input("Enter the 1st base: ")

    t2_base = input("Enter the 2nd base: ")

    trap_height = input("Enter the height of the trapezoid: ")
    trap_area = ((int(t1_base) + int(t2_base)) / 2) * int(trap_height)
    print("trapezoid: ", "base 1 =", t1_base, "base 2 =", t2_base, "area =", trap_area)

def main():
    circle()
    sphere()
    rectangle()
    square()
    isosceles_triangle()
    equilateral_triangle()
    trapezoid()

main()
