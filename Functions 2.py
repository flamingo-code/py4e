print ("Functions 2")
print ("LIS 161 - PJ Perez")
print ("Rad Julongbayan")
def computegrade(score):
    if score<0.0 or score>1.0:
        print("Bad Score, please enter a numeric score between 0.0 and 1.0.")
        quit()
    elif score>=0.9:
        grade="A"
    elif score>=0.8:
        grade="B"
    elif score>=0.7:
        grade="C"
    elif score>=0.6:
        grade="D"
    elif score<0.6:
        grade="F"
    return grade

x=input("Enter score between 0.0 and 1.0: ")
try:
    score=float(x)
except:
    print("Bad Score, please enter a numeric score between 0.0 and 1.0.")
    quit()

gradeletter=computegrade(score)
print("Grade: ", gradeletter)
