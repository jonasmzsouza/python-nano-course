from function import *

myList=[]

print("Filling in...")
fillInventory(myList)

print("\nDisplaying in...")
diplayInventory(myList)

print("\nSearching...")
searchElement(myList)

print("\nChanging...")
p = int(input("Enter a number for the percentage: "))
changeElement(myList, p)

print("\nDeleting...")
print(deleteElement(myList))
diplayInventory(myList)

print("\nSumming up...")
summaryValues(myList)