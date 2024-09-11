'''total = 0

for x in range(4):
    total = total + x 

print(total)'''

'''animals = ["porcupines", "hedgehogs", "sea urchins", "Lionfish"]

for x in animals:
    print(x + "is the spikiest animal ever! ")'''


'''start = int(input("Enter a number "))
end = int(input("Enter aother number "))

total_sum = 0

for x in range(start, end + 0):
    total_sum += x 

print(total_sum)'''

var1 = int(input("Enter the first integer (var1) "))
var2 = int(input("Enter the second integer (var2) "))


if var1 < var2:
 
    for number in range(var1, var2 + 1):
        print(number, end=" ")
else:
    print("Please ensure that var1 is less than var2.")