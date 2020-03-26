with open("./files/file-test.txt", "w") as file:
  file.write("Creating a file has never been easier.")

with open("file-test.txt", "a") as file:
  file.write("\n...Continue")