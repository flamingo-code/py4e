print ("Conditional Statements 2")
print ("LIS 161 - PJ Perez")
print ("Rad Julongbayan")
x=input("Enter Hours: ")
try:
    hours=float(x)
except:
    print("Error, please enter numeric input")
    quit()

y=input("Enter Rate: ")
try:
    rate=float(y)
except:
    print("Error, please enter numeric input")
    quit()

if hours>40:
    excess=hours-40
    total=(40*rate)+(excess*rate*1.5)
else:
    total=hours*rate
print("Pay:",total)
