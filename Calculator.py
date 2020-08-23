while True:
    print("Choose one of the option below and enter your input:- \nExample:If your option is Average type 2\n")
    print("1.Simple Calculator : /, * , + , -")
    print("2.Average")
    print("3.Percentage")
    print('4.Area')
    print("5.Profit & Loss")
    print('6.exit')
    #The below variable will ask the input from the user.
    main_input=input("Enter your input: ")

    if main_input=='1':
        while True:
            print("Choose your operator below")
            print("1.Sum")
            print("2.Sub")
            print("3.Div")
            print("4.Product")
            print('5.Reminder')
            print("0.To go back to previous section")
            #the below option will collect the selection options for Simple Calculator
            select_simple = (input("enter your input"))



            def sum(x,y):
                print (x+y)

            def sub(x,y):
                print (x-y)

            def div(x,y):
                print (x/y)

            def product(x,y):
                print(x*y)

            def reminder(x,y):
                print(x%y)


            if select_simple=="0":
                break

            if select_simple=="1":
                try:
                    print("You selected 'Sum',press enter you wanna choose something else")
                    number1=int(input("enter your first number"))
                    number2=int(input("Enter second number"))
                    sum(number1,number2)
                    print()

                except:
                    print("Invalid input")
            if select_simple=="2":
                try:
                    print("You selected 'Sub',press enter you wanna choose something else")
                    number1=int(input("enter your first number"))
                    number2=int(input("Enter second number"))
                    sub(number1,number2)
                except:
                    print("Invalid input")
            if select_simple=="3" :
                try:
                    print("You selected 'Div',press enter you wanna choose something else")
                    number1=int(input("enter your first number"))
                    number2=int(input("Enter second number"))
                    div(number1,number2)
                except:
                    print("Invalid input")
            if select_simple=="4" :
                try:
                    print("You selected 'Product',press enter you wanna choose something else")
                    number1=int(input("enter your first number"))
                    number2=int(input("Enter second number"))
                    product(number1,number2)
                except:
                    print("Invalid input")
            if select_simple == "5":
                try:
                    print("You selected 'Reminder',press enter you wanna choose something else")
                    number1=int(input("enter your first number"))
                    number2=int(input("Enter second number"))
                    reminder(number1,number2)
                except:
                    print("Invalid input!\nPlease try again!")
            if select_simple not in ['1','2','3','4','5','0']:
                print("invalid input!")

    if main_input=="2":
        while True:
            num = int(input('How many numbers: '))
            total_sum = 0
            for n in range(num):
                numbers = float(input('Enter number : '))
                total_sum += numbers
            avg = total_sum/num
            print('Average of ', num, ' numbers is :', avg,"\n \n \n")


            break


    if main_input=="3":
        while True:
            val1=(input("Enter your value: "))
            value=float(val1)
            totval=(input("please enter your total value here: "))
            total=float(totval)

            perecentageee=(value/total)*100
            print("Value =",val1,"Total value =",totval,"\npercentage =",perecentageee,"%")

            back_percent=input("if you wanna return back to previous menu type back or press enter").lower()
            if back_percent=='back':
                break
    if main_input=="4":
        while True:
            print("Choose one of the option below and enter your input:- \nExample:If your option is sqare type 3\n")
            print('1.Triangle')
            print("2.rectangle")
            print("3.Square")
            print("4.Cone")
            print("5.Cube")
            print("6.Cuboid")
            print("7.Circle")
            print("8.Cylinder")
            print("9.go back to main menu")


            area_input=input("Enter your input here: ")

            if area_input=='1':
                 while True:
                    base=float(input("Enter the value for your base"))
                    height=float(input('Enter the hieght of your triangle'))
                    tri=((1/2)*base*height)

                    print ("the area of triangle =",tri)
            #print (tri) is the value for area of the triangle
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break

            if area_input=='2':
                while True:
                    base=float(input("Enter the value for your base:"))
                    height=float(input("enter your height here"))
                    rectangle=(base*height)

                    print("the area of rectangle =",rectangle)

                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break

            if area_input=='3':
                while True:
                    side=float(input('enter the side of the square'))

                    area = side**2
                    print("the area of square =",area)
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break
            if area_input=='4':
                while True:
                    radius= float(input('enter the radius of the cone'))
                    height= float(input('enter the hieght of the cone'))

                    area_of_cone= float(((22/7)*radius)(radius+(radius+height)))
                    print("area of cone =",area_of_cone)
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break
            if area_input=='5':
                while True:
                    side=input("enter the side of the cubea")
                    are_cube=side**3
                    print("area of cube =",are_cube)
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break
            if area_input=="6":
                while True:
                    l=float(input('enter the lenth: '))
                    b=float(input("enter the breadth: "))
                    h=float(input("enter the height: "))

                    area_of_cuboid=(l*b*h)

                    print("area of cuboid =",area_of_cuboid)
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break

            if area_input=='7':
                while True:
                    rr=float(input('Enter the radius of the circle'))

                    area_of_circle=22/7*rr**2
                    print (area_of_circle)
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break


            if area_input=="8":
                while True:
                    radius=float(input("enter the radius of the cylinder: "))
                    height=float(input("enter the height of the cylinder: "))
                    area_of_cyl=(22/7)*(radius**2)*height
                    print("the area of the cylinder =",area_of_cyl)
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                            break
                    if area_input=='9':
                        break

    if main_input=="5":
        while True:
            print("Choose one of the option below and enter your input:- \nExample:If your option is Gain type 1\n")
            print("1.Gain %")
            print("2.Loss %")
            print("3.Selling Price Loss")
            print("4.Selling Price Profit")
            p_loss=input("please enter your input here or type back to go back.")


            if p_loss =="1":
                while True:
                    print("you have selected Gain%.")
                    gain=float(input("Enter the value for 'gain' here: "))
                    cost_price=float(input("Enter the value for 'cost_price' here: "))
                    gainpercent=(gain/cost_price)*100
                    print("Gain% =",gainpercent)
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break
                    if area_input=='9':
                        break
            if p_loss=="2":
                while True:
                    print("you have selected Loss%.")
                    loss=float(input("Enter the value for 'loss' here: "))
                    cost_price=float(input("Enter the value for 'cost_price' here: "))
                    losspercent=(loss/cost_price)*100
                    print("loss% =",losspercent)
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break

            if p_loss=="3":
                while True:
                    print("you have selected Selling Price Loss.")
                    loss=float(input("Enter the value for 'Loss%' here: "))
                    cost_price=float(input("enter the value for 'cost_price' here"))
                    SPL=((100-loss)/100)*cost_price
                    print("Selling Price =",SPL)
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break
            if p_loss=="4":
                while True:
                    print("you have selected Selling Price Profit.")
                    gain=float(input("Enter the value for 'Profit%' here: "))
                    cost_price=float(input("enter the value for 'cost_price' here"))
                    SPL=((100+gain)/100)*cost_price
                    print("Selling Price =",SPL)
                    tri_exit=input("type back if you wanna go back to the previous menu or press enter to continue").lower()
                    if tri_exit=="back":
                        break
            if p_loss not in["1","2","3","4","back"]:
                print("invalid input.")

    if main_input=="6":
        quit()
    if main_input not in["1","2","3","4","5","6"]:
        print("Invalid input.")
