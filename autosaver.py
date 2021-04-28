import os


PATH="/home/ramesh/Downloads/Python/"
# print(os.listdir(PATH))



FILE_NAME=input("Filename : ")
EXTENSION=".py"
COMPLETEPATH=PATH+FILE_NAME+EXTENSION

# print(COMPLETEPATH)
with open(COMPLETEPATH,'w'):
    if os.path.exists(COMPLETEPATH):
#         print("True")
        print("Mission Success Bro!!..Go Ahead!")