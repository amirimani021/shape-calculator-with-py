# index.py app    

                                                 

print('Hello ! welcome to Amir app please choose one of this :')                          

print('circle code number :1 , recteangle code number:2 , squre code number:3 triangle code number:4')    # code numbers       

code = input("enter your code :")                                 # code input

code = int(code)                                  # code type
   

if code < 2 and code > 0 :                      # circle if code

    radius = input("please give me your radius :")               # radius input      

    radius = int(radius)                        # radius type
    
    pi = 3.14                                # pi
    
    circle_area = (radius**2)*pi           # circle area formula
    
    circle_perimeter = (2*pi)*radius           # circle environment formula
    
    print("your circle area is :" , circle_area)          # print of output area
    
    print('your circle perimeter is:' , circle_perimeter)    # print of output environment

elif code>1 and code<3 :                    # rectangle if code

    width = input('please give me your width :')       # width input

    width = int(width)                 # width type

    the_length = input('please give me your your length :')    # the length input

    the_length = int(the_length)          # the length type

    rectangle_area = (width*the_length)        # rectangle area formula 

    rectangle_perimeter = (width + the_length)*2      # recteangle environment formula

    if width>the_length :                     # if code of width and the length rectangle

        rectangle_area = False             # false area

        rectangle_perimeter = False           # false environment

        print('is not true becuse width a more of the length')      # if print 

    print("your rectangle area is:" , rectangle_area)         # print output of rectangle area

    print('your rectangle perimeter is:' , rectangle_perimeter)       #print output pf rectangle environment

elif code < 4 and code > 2 :   
    
    squre_side = input('please give me your squre side :')

    squre_side = int(squre_side)

    squre_perimeter = (4 * squre_side)

    squre_area = (squre_side * squre_side)

    print('your squre area is :' , squre_area)

    print('your squre oerimeter is :' , squre_perimeter)

elif code < 6 and code > 3 :

    triangle_first_side = input("plese give me your first side :")

    triangle_first_side = int(triangle_first_side)

    triangle_second_side = input("plese give me your second side :")

    triangle_second_side = int(triangle_second_side)

    triangle_base = input("plese give me your base :")

    triangle_base = int(triangle_base)

    triangle_height = input("plese give me your height :")

    triangle_height = int(triangle_height)

    triangle_primeter = (triangle_first_side + triangle_second_side + triangle_base)

    triangle_area = (triangle_height * triangle_base) / 2

    print("your triangle area is :" , triangle_area)

    print("your triangle perimeter is :" , triangle_primeter)
else :
   print("code is false")   

input("Press enter to exit ;)")