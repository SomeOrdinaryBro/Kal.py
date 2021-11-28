#calculating the salary perday
PRHR = input('How Much Do You Get Paid Per-Hour: ')
HRSPD = input('How Many Hours do you Work Per-day: ')
PRDAYSAL = float(PRHR) * float(HRSPD) 

#calculating the salary permonth using 'PRDAYSAL' from above code
DYSLBR = input('How manys did you work this month? ')

#Using DYSLBR multiplied to PRDAYSAL the code below will find the users monthly salary & per day salary
print(PRDAYSAL, 'Is your Per Day Salary')

MTHLYPAY = float(PRDAYSAL) * float(DYSLBR)
print(MTHLYPAY, 'this Should be your Salary This Month')
