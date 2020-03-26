with open("./files/page-test.html", "w") as page:
    page.write("<body> <h1> This is a test for the web page </h1>")
    page.write("<br><h2> Below are some important names for the project:  </h2>")
    page.write("<h3>")
    name=""
    while name!="EXIT":
        name = input("Enter a name or EXIT: ").upper()
        if name!="EXIT":
            page.write("<br>"+name)
    page.write("</h3></body>")