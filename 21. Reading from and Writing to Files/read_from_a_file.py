# cupcakes_fils = open("cupcakes.txt", "r")
# # faulty code
# cupcakes_fils.close()


# with open("21. Reading from and Writing to Files\cupcakes.txt", "r") as cupcakes_file:
#     print("The file has been opened!")
#     content = cupcakes_file.read()
#     print(content)
    
# print("The file has been closed. We are outside the blcok!")


filename = input("What file would you like to open? ")
with open(filename, "r") as file_object:
    print(file_object.read())

