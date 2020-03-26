with open("./files/file-test.txt", "rt") as file:
    content=file.readlines()
print("Variable data type", type(content))
print("\nFile content:\n", content)