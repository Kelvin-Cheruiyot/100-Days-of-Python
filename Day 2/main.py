print("Welcome to the tip calculator.")
tb=float(input("What was your total bill? $"))
pt=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
s=int(input("How many people to split the bill? "))
tt=pt/100+1
ntb=tb*tt
pay="{:.2f}".format(ntb/s)
print(f'Each person should pay: ${pay}')