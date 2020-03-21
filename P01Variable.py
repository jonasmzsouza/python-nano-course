name=input("Enter an employees: ")
company=input("Enter a company name: ")
quantityEmployees=int(input("Enter the number of employees: "))
monthlyAverage=float(input("Enter the monthly payment average: "))

print("\n" + name + " works at the company " + company)
print("He has ", quantityEmployees," employees.")
print("The monthly payment average is: " + str(monthlyAverage))

print("\n[name] is variable data type: ",type(name))
print("[company] is variable data type: ",type(company))
print("[quantityEmployees] is Variable data type: ",type(quantityEmployees))
print("[monthlyAverage] is Variable data type: ",type(monthlyAverage))