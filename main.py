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


def hlp():
  print('Currently we have 5 different applications under this')
  print('please contact the repo owner to use this in your project')

def ShapesKal():
  def Circle():                
      print("Select operation.")
      print("1.Diameter")
      print("2.Circumference")
      print("3.Area")
      choice = input("Enter choice(1/2/3): ")
  
      if choice in ('1', '2', '3'):
        
          if choice == '1':
              PI = 3.14
              radius = float(input(' Please Enter the radius of a circle: '))
  
              diameter = 2 * radius
              print(" \nDiameter Of a Circle = %.2f" %diameter)
              
          elif choice == '2':
              PI = 3.14
              radius = float(input(' Please Enter the radius of a circle: '))
  
              circumference = 2 * PI * radius
              print(" Circumference Of a Circle = %.2f" %circumference)
  
          elif choice == '3':
              PI = 3.14
              radius = float(input(' Please Enter the radius of a circle: '))
  
              area = PI * radius * radius
              print(" Area Of a Circle = %.2f" %area)
  
  def Square(): 
      print("Select operation.")
      print("1.Perimeter")
      print("2.Area")
      choice = input("Enter choice(1/2): ")
  
      if choice in ('1', '2'):
        
          if choice == '1':
              s=int(input("How Many Sides Does Your Squre Have : "))
              area=s*s
              print("Area of Square : ",area)
              
          elif choice == '2':
              s=int(input("How Many Sides Does Your Squre Have : "))
              perimeter=4*s
              print("Perimeter of Square : ",perimeter)
  
  def Rectangle():
      print("Select operation.")
      print("1.Perimeter")
      print("2.Area")
      choice = input("Enter choice[1/2]: ")
  
      if choice in ('1', '2'):
        
          if choice == '1':
              l=int(input("Length : "))
              w=int(input("Width : "))
              area=l*w
              print("Area of Rectangle : ",area)
  
          elif choice == '2':
              l=int(input("Length : "))
              w=int(input("Width : "))
              perimeter=2*(l+w)
              print("Perimeter of Rectangle : ",perimeter)
  
  print("Select operation.")
  print("1.Circle")
  print("2.Square")
  print("2.Rectangle")
  
  
  while True:
      choice = input("Enter choice(1/2/3): ")
  
      if choice in ('1', '2', '3'):
        
          if choice == '1':
              Circle()
  
          elif choice == '2':
              Square()
  
          elif choice == '3':
              Rectangle()

def NormalKal():
  def add(A, B):
      return A + B
  def subtract(A, B):
      return A - B
  def multiply(A, B):
      return A * B
  def divide(A, B):
      return A / B
  
  print("What Type Of Calculation Would You Like to do Today?")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  
  while True:
      choice = input("Please type your choice [1/2/3/4]: ")
      print("---------------------------------------------")
    
      if choice in ('1', '2', '3', '4'):

          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
  
          if choice == '1':
              print(num1, "+", num2, "=", add(num1, num2))
          elif choice == '2':
              print(num1, "-", num2, "=", subtract(num1, num2))
          elif choice == '3':
              print(num1, "*", num2, "=", multiply(num1, num2))
          elif choice == '4':
              print(num1, "/", num2, "=", divide(num1, num2))
            

def LoanKal():
  def f1 (principle,annual_interest_rate,duration):
    r = annual_interest_rate/1200
    n = duration*12
    a=principle*r*((1+r)**n)
    b= (((1+r)**n)- 1)
    if r > 0 :
        MonthlyPayment = (a/b)
    else :
        MonthlyPayment = principle/n

    return MonthlyPayment

  def f2 (principle,annual_interest_rate,duration,number_of_payments):
      r = annual_interest_rate/1200
      n = duration*12
      a= ((1+r)**n)
      b= ((1+r)**number_of_payments)
      c= (((1+r)**n)-1)
      if r > 0 :
          RemainingLoanBalance = principle*((a-b)/c)
      else :
          RemainingLoanBalance = principle*(1-(number_of_payments/n))
  
      return RemainingLoanBalance

  principle=float(input("Enter loan amount: "))
  annual_interest_rate=float(input("Enter annual interest rate (percent): "))
  duration=int(input("Enter loan duration in years: "))
  
  print ("LOAN AMOUNT:",principle,"INTEREST RATE (PERCENT):",annual_interest_rate)
  print ("DURATION (YEARS):",duration,"MONTHLY PAYMENT:",int(f1(principle,annual_interest_rate,duration)))

def CurrecyKal():
  print('')
  print('Coming Soon!!')
  print('')
  print('in the meantime, try out our other calculators')
  print(" ")
  print("Select 1 -  Salary Calculator")
  print("Select 2 -  Calculate Shapes ")
  print("Select 3 -  Calculator ")  
  print("Select 4 -  Loan Calculator ")  
  print("-----------------------------------------------------")  
  choice = input("Enter Your choice [1/2/3/4]: ")

  
  if choice in ('1', '2','3','4'):
      
      if choice == '1':
          SalarayKal()

      elif choice == '2':
          ShapesKal()

      elif choice == '3':
          NormalKal() 
          
      elif choice == '4':
          LoanKal()  
    
      else:
          print("Please enter a valid option")

while True:
    print("What Kind Of Calculation Would You Like To Do Today?")
    print("-----------------------------------------------------")
    print(" ")
    print("Select 1 -  Salary Calculator")
    print("Select 2 -  Calculate Shapes ")
    print("Select 3 -  Normal Calculator ")  
    print("Select 4 -  Loan Calculator ")  
    print("Select 5 -  Currency Calculator - W.I.P")  
    print("type > HELP -- for more information")
    print("-----------------------------------------------------")  
    choice = input("Enter Your choice [1/2/3/4/5]: ")

  
    if choice in ('1', '2', '3', '4', '5', 'HELP'):
      
        if choice == '1':
            SalarayKal()

        elif choice == '2':
            ShapesKal()

        elif choice == '3':
            NormalKal() 
          
        elif choice == '4':
            LoanKal()  

        elif choice == '5':
            CurrecyKal() 

        elif choice == 'HELP':
            hlp()
      
        next_calculation = input("Would You Like To Do  Calculation? (YES/NO): ")
        if next_calculation == "NO":
            break
        if next_calculation == "No":
            break
        if next_calculation == "nO":
            break
        if next_calculation == "No":
            break