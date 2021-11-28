class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#calculating the salary perday
PRHR = input('How Much Do You Get Paid Per-Hour: ')
HRSPD = input('How Many Hours do you Work Per-day: ')
PRDAYSAL = float(PRHR) * float(HRSPD) 

#calculating the salary permonth using 'PRDAYSAL' from above code
DYSLBR = input('How manys did you work this month? ')

MTHLYPAY = float(PRDAYSAL) * float(DYSLBR)
#print(MTHLYPAY, 'this Should be your Salary This Month')

print(MTHLYPAY, (color.GREEN + 'is your Monthly Salary' + color.END))
