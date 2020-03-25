ips={}
answer="Y"
while answer=="Y":
    ips[(input("Enter the first two octets: "),
       input("Enter the last two octets: "))]=input("\nMachine name: ")
    answer=input("\nEnter <Y> to continue: ").upper()

print("\nDisplaying IPs: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("\nDisplay machines with the same address: ")
search=input("Enter the last two octets: ")
print("Machines at the same address (different networks)")
for ip,name in ips.items():
    if(ip[1]==search):
        print(name)

print("\nThe machines that make up the same network: ")
network=input("Enter the first two octets: ")
for ip,name in ips.items():
    if(ip[0]==network):
        print(name)