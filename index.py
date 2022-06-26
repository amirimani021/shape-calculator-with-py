# index.py app


print('Hello ! welcome to Amir app please choose one of this :')

# code numbers
print('circle code number :1 , rectangle code number:2 , square code number:3 triangle code number:4')

code = input("enter your code :")                                 # code input

code = int(code)                                  # code type


#--------------------------Functions----------------------------------#
def circle():

    radius = input("please give me your radius :")               # radius input

    radius = int(radius)                        # radius type

    pi = 3.14                                # pi

    circle_area = (radius**2)*pi           # circle area formula

    circle_perimeter = (2*pi)*radius           # circle environment formula

    print("your circle area is :", circle_area)          # print of output area

    # print of output environment
    print('your circle perimeter is:', circle_perimeter)


def rectangle():

    width = input('please give me your width :')       # width input

    width = int(width)                 # width type

    # the length input
    the_length = input('please give me your your length :')

    the_length = int(the_length)          # the length type

    rectangle_area = (width*the_length)        # rectangle area formula

    # recteangle environment formula
    rectangle_perimeter = (width + the_length)*2

    if width > the_length:                     # if code of width and the length rectangle

        rectangle_area = False             # false area

        rectangle_perimeter = False           # false environment

        print('is not true becuse width a more of the length')      # if print

    # print output of rectangle area
    print("your rectangle area is:", rectangle_area)

    # print output pf rectangle environment
    print('your rectangle perimeter is:', rectangle_perimeter)


def square():

    square_side = input('please give me your square side :')

    square_side = int(square_side)

    square_perimeter = (4 * square_side)

    square_area = (square_side * square_side)

    print('your square area is :', square_area)

    print('your square oerimeter is :', square_perimeter)


def triangle():

    triangle_first_side = input("plese give me your first side :")

    triangle_first_side = int(triangle_first_side)

    triangle_second_side = input("plese give me your second side :")

    triangle_second_side = int(triangle_second_side)

    triangle_base = input("plese give me your base :")

    triangle_base = int(triangle_base)

    triangle_height = input("plese give me your height :")

    triangle_height = int(triangle_height)

    triangle_primeter = (triangle_first_side +
                         triangle_second_side + triangle_base)

    triangle_area = (triangle_height * triangle_base) / 2

    print("your triangle area is :", triangle_area)

    print("your triangle perimeter is :", triangle_primeter)
#--------------------------End of functions----------------------------------#


if code == 1:                      # circle if code
    circle()


elif code == 2:                    # rectangle if code
    rectangle()


elif code == 3:                   # square if code
    square()


elif code == 4:                   # triangle if code
    triangle()


else:  # if non of above
    print("code is false")


input("Press enter to exit ;)")  # to prevent the cmd from closing
