print ("Functions 1")
print ("LIS 161 - PJ Perez")
print ("Rad Julongbayan")
def computepay(hours, rate):
    if hours>40:
        excess=hours-40
        total=(40*rate)+(excess*rate*1.5)
    else:
        total=hours*rate
    return total

x=input("Enter Hours: ")
y=input("Enter Rate: ")
hours=float(x)
rate=float(y)

payment=computepay(hours, rate)
print("Pay:", payment)
