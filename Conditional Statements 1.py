print ("Conditional Statements 1")
print ("LIS 161 - PJ Perez")
print ("Rad Julongbayan")
x=input("Enter Hours: ")
y=input("Enter Rate: ")
hours=float(x)
rate=float(y)
if hours>40:
    excess=(hours-40)
    total=(40*rate)+(excess*rate*1.5)
else:
    total=hours*rate
print ("Pay:",total)
