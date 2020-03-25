number=int(input("Enter a number to display the multiplication table. "))
print("Number multiplication table: ", number)
for i in range(1,11,1):
    print(str(number) + " X " + str(i) + " = " + str(number*i))


