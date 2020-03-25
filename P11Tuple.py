ips={}
answer="Y"
while answer=="Y":
    ips[(input("Enter the first two octets: "),
       input("Enter the last two octets: "))]=input("\nMachine name: ")
    answer=input("\nEnter <Y> to continue: ").upper()

print("\nDisplaying IPs: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])