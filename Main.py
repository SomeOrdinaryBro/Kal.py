def SalarayKal():
  def CAPITAL_OUTPUT1():
     print("\n\n")
     print("          Y O U R      -      S A L A R Y -      D E T A I L S ")
     print("================================================================================")
     print("YOUR PER-DAY SALARY: ", float(PRDAYSAL), (color.GREEN + 'is your per-day salary' + color.END))
     print("YOUR BASIC SALARY: ", int(MTHLYPAY), (color.GREEN + 'is your Monthly Salary' + color.END))
     print("YOUR MONTHLY SALARY: ", float(SALWITHEPF), (color.GREEN + 'is your Salary in hand with 8% Contribution to EPF' + color.END))
     print("================================================================================")
  
  def CAPITAL_OUTPUT2():
     print("\n\n")
     print("          Y O U R      -      S A L A R Y -      D E T A I L S ")
     print("================================================================================")
     print("YOUR PER-DAY SALARY: ", float(PRDAYSAL), (color.GREEN + 'is your per-day salary' + color.END))
     print("YOUR BASIC SALARY: ", int(MTHLYPAY), (color.GREEN + 'is your Monthly Salary' + color.END))
     print("================================================================================")
  
  
  
  
  
  
  #NOT USING THIS SINCE IM USING A ASCII OUTPUT BELOW... SORT OF..
  #print(PRDAYSAL, (color.GREEN + 'is your per-day salary' + color.END))
  #print(MTHLYPAY, (color.GREEN + 'is your Monthly Salary' + color.END))
  
  class color:
     GREEN = '\033[92m'
     BOLD = '\033[1m'
     END = '\033[0m'
  
  PRHR = input('How Much Do You Get Paid Per-Hour: ')
  HRSPD = input('How Many Hours do you Work Per-day: ')
  PRDAYSAL = float(PRHR) * float(HRSPD) 
  
  DYSLBR = input('How manys did you work this month? ')
  
  MTHLYPAY = int(PRDAYSAL) * int(DYSLBR)
  
  
  EPF = input('Does your workplace require you to contribute to EPF? (please type YES/NO) ')
  
  if EPF == "YES": 
     EPFCUTS = 8
     MTHLYPAYSS = MTHLYPAY
     SALWITHEPF = int(MTHLYPAYSS) - int(MTHLYPAYSS) * float(EPFCUTS) / 100
  
     CAPITAL_OUTPUT1()
  
  elif EPF == ("NO"):
     CAPITAL_OUTPUT2()
  
  
  if EPF == "yes": 
     EPFCUTS = 8
     MTHLYPAYSS = MTHLYPAY
     SALWITHEPF = int(MTHLYPAYSS) - int(MTHLYPAYSS) * float(EPFCUTS) / 100
  
     CAPITAL_OUTPUT1()
  
  elif EPF == ("no"):
     CAPITAL_OUTPUT2()
  
  input()
  
def Circle():
    print(" ")
    print("Select an opration to Perform")
    print(" ")
    print("1.Diameter")
    print("2.Circumference")
    print("3.Area")
    print(" ")
    choice = input("Enter Your choice [1/2/3]: ")

    if choice in ('1', '2', '3'):

        if choice == '1':
            PI = 3.14
            radius = float(input('Please Enter the radius of a circle: '))

            diameter = 2 * radius
            print(" \nDiameter Of a Circle = %.2f" % diameter)

        elif choice == '2':
            PI = 3.14
            radius = float(input(' Please Enter the radius of a circle: '))

            circumference = 2 * PI * radius
            print(" Circumference Of a Circle = %.2f" % circumference)

        elif choice == '3':
            PI = 3.14
            radius = float(input(' Please Enter the radius of a circle: '))

            area = PI * radius * radius
            print(" Area Of a Circle = %.2f" % area)


def Square():
    print(" ")
    print("Select an opration to Perform")
    print(" ")
    print("1.Perimeter")
    print("2.Area")
    print(" ")
    choice = input("Enter Your choice [1/2]: ")

    if choice in ('1', '2'):

        if choice == '1':
            s = int(input("How Many Sides Does Your Squre Have : "))
            area = s * s
            print("Area of Square : ", area)

        elif choice == '2':
            s = int(input("How Many Sides Does Your Squre Have : "))
            perimeter = 4 * s
            print("Perimeter of Square : ", perimeter)


def Rectangle():
    print(" ")
    print("Select an opration to Perform")
    print(" ")
    print("1.Perimeter")
    print("2.Area")
    print(" ")
    choice = input("Enter Your choice [1/2]: ")

    if choice in ('1', '2'):

        if choice == '1':
            l = int(input("Length : "))
            w = int(input("Width : "))
            area = l * w
            print("Area of Rectangle : ", area)

        elif choice == '2':
            l = int(input("Length : "))
            w = int(input("Width : "))
            perimeter = 2 * (l + w)
            print("Perimeter of Rectangle : ", perimeter)


while True:
    print(".......................................")
    print("Select A Shape to Perform Calculation's")
    print(".......................................")
    print(" ")
    print("1.Circle")
    print("2.Square")
    print("2.Rectangle")
    print(" ")

    choice = input("Enter Your choice [1/2/3] : ")

    if choice in ('1', '2', '3'):

        if choice == '1':
            Circle()

        elif choice == '2':
            Square()

        elif choice == '3':
            Rectangle()

        next_calculation = input("Would You Like To Do Another Calculation? (YES/NO): ")
        if next_calculation == "NO":
          break
        if next_calculation == "no":
          break
        if next_calculation == "nO":
          break
        if next_calculation == "No":
          break
        else:
          print("Invalid Input")
