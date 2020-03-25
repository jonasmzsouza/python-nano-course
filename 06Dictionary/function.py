def ask():
    answer = input("\nWhat do you want to do?\n" +
                   "<I> - To insert an user\n" +
                   "<S> - To search an user\n" +
                   "<D> - To delete an user\n" +
                   "<L> - To list an user\n").upper()
    return answer

def insert(dictionary):
    dictionary[input("Enter a login: ").upper()] = [input("Enter a name: ").upper(),
                                               input("Enter the last access date: "),
                                               input("Enter the last access terminal: ")]

def search(dictionary, key):
    list=dictionary.get(key)
    if list!=None:
        print("Name.................: " + list[0])
        print("Last access..........: " + list[1])
        print("Last terminal........: " + list[2])

def delete(dictionary, key):
    if dictionary.get(key)!=None:
        del dictionary[key]
    print("Deleted object")

def list(dictionary):
    for key, value in dictionary.items():
        print("........................................")
        print("Login: ", key)
        print("Data: ", value)
        print("........................................")