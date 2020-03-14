print ("Iterations 2")
print ("LIS 161 - PJ Perez")
print ("Rad Julongbayan")

count = 0
total = 0
smallest = "extremes"
largest = "extremes"

while True:
    number = input("Enter a number: ")
    try:
        value = float(number)
    except:
        if number == 'done':
          break
        else:
          print ('Invalid Input')
          continue
    if smallest == "extremes":
        smallest = value
    elif value < smallest:
        smallest = value
    if largest == "extremes":
        largest = value
    elif value > largest:
        largest= value

count = count + 1
total = total + value

print("Total: ", total)
print("Number of Entries: ", count)
print("Maximum Number: ", largest)
print("Minumum Number: ", smallest)
