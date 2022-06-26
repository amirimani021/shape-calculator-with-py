import os
# def color(): return os.system('color a')


def clear(): return os.system('cls')


def main():
    os.system('color 02')
    print(' Hello! Welcome to the Shape Calculator \n Please choose one of these codes:\n')

    # code numbers
    print(' Circle code number: 1 \n Rectangle code number: 2 \n Square code number: 3 \n Triangle code number: 4\n')

    # code input
    code = input(" Enter your code : ")

    try:
        code = int(code)
    except:
        pass

    # while not valid:  # loop until the user enters a valid int
    #     try:
    #         x = int(input('Enter an integer: '))
    #         valid = True  # if this point is reached, x is a valid int
    #     except ValueError:
    #         print('Please only input digits')

    #--------------------------Functions----------------------------------#

    def circle():

        # radius input
        radius = int(input(" Please give me your radius : "))

        pi = 3.14                                # pi

        circle_area = (radius**2)*pi           # circle area formula

        circle_perimeter = (2*pi)*radius           # circle environment formula

        # print of output area
        print(" Your circle area is : ", circle_area)

        # print of output environment
        print(' Your circle perimeter is: ', circle_perimeter)

    def rectangle():

        width = int(input(' Please give me your width : '))       # width input

        # the length input
        the_length = input(' Please give me your your length : ')

        the_length = int(the_length)          # the length type

        rectangle_area = (width*the_length)        # rectangle area formula

        # rectangle environment formula
        rectangle_perimeter = (width + the_length)*2

        if width > the_length:      # if code of width and the length rectangle
            return print(" This calculation is not possible")

        else:

            # print output of rectangle area
            print(" Your rectangle area is:", rectangle_area)

            # print output pf rectangle environment
            print(' Your rectangle perimeter is:', rectangle_perimeter)

    def square():

        square_side = int(input(' Please give me your square side : '))

        square_perimeter = (4 * square_side)

        square_area = (square_side * square_side)

        print(' Your square area is : ', square_area)

        print(' Your square oerimeter is : ', square_perimeter)

    def triangle():

        triangle_first_side = int(input(" Please give me your first side : "))

        triangle_second_side = int(
            input(" Please give me your second side : "))

        triangle_base = int(input(" Please give me your base : "))

        triangle_height = int(input(" Please give me your height : "))

        triangle_primeter = (triangle_first_side +
                             triangle_second_side + triangle_base)

        triangle_area = (triangle_height * triangle_base) / 2

        print(" Your triangle area is : ", triangle_area)

        print(" Your triangle perimeter is : ", triangle_primeter)
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
        print(" Code is invalid!")

    # to prevent the cmd from closing
    nextUp = int(input("\n Enter 1 to return , press enter to exit: "))

    if nextUp == 1:
        clear()
        main()

    else:
        exit()


main()
