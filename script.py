class Triangle:
    number_of_sides = 3
    
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def __str__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        return str(number_of_sides)

    def check_angles(self, angle1, angle2, angle3):
        if angle1 + angle2 + angle3 == 180:
            return True
        else:
            return False

    def __eq__(self):
        if self.angle1 == self.angle2:
            bool1 = True
        else:
            bool1 = False

        if self.angle2 == self.angle3:
            bool2 = True
        else:
            bool2 = False

        if bool1 and bool2:
            return True
        else:
            return False


angle1 = float(input("Podaj pierwszy kat: "))
angle2 = float(input("Podaj drugi kat: "))
angle3 = float(input("Podaj trzeci kat: "))

my_triangle = Triangle(angle1, angle2, angle3)
print("\nMoj trojkat ma {} boki\n".format(str(my_triangle.number_of_sides)))

if my_triangle.check_angles(angle1, angle2, angle3):
    print("i katy {} {} {} go tworza\n".format(angle1, angle2, angle3))
else:
    print("i katy {} {} {} go nie tworza\n".format(angle1, angle2, angle3))

if my_triangle.__eq__():
    print("Katy sa takie same\n")
else:
    print("Katy sa inne\n")