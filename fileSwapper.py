Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def fileSwapper():
    fileName = input("Name the file which you want to get data from: ")
    fileNameB = input("Name the other file which you want to get data from: ")
    with open(fileName, "r") as a:
        data_a = a.read()
    with open(fileNameB, "r") as b:
        data_b = b.read()
    with open(fileName, "w") as a:
        a.write(data_b)
        print("The first file says", data_b)
        print("The second file says", data_a)
        print("I hope the files did not get swapped ;)")

        
