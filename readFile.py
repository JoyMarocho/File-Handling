# Reading a file
# handle = open("test.txt","r")

# data = handle.read()
# print(data)

# handle.close()



# Reading a single line
# handle = open("test.txt","r")

# data = handle.readline()
# print(data)

# handle.close()


# Reading multiple lines
# handle = open("test.txt","r")

# data = handle.readlines()
# print(data)

# handle.close()

# Looping trough a files
# handle = open("test.txt","r")
# data = handle.read()
# counter = 0
# for word in data.split():
#     if word == "Python":
#         counter += 1

# print(counter)



#  WRITING A FILE
# handle = open("text-write.txt", "w")

# handle.write("Hello Moringa")
# handle.close()


# Wtinging a text 
# with operator
with open("test.txt","r") as handle:
    data = handle.read()
    print(data)