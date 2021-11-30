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
