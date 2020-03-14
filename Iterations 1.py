print ("Iterations 2")
print ("LIS 161 - PJ Perez")
print ("Rad Julongbayan")

count = 0
total = 0

while True:
    number= input("Enter a number: ")
    try:
        value = float(number)
    except:
        if number == 'done':
          break
        else:
          print ('Invalid Input')
          continue
    count = count + 1
    total = total + value
print("Total: ", total)
print("Number of Entries: ", count)
print("Average: ", total/count)
