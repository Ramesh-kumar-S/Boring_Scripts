import sys

# print("No of Argvs :",len(sys.argv))
# print("Name of the Script :",sys.argv[0])
print(sys.argv)
print("\nArguments Passed :\n",end =" ")
for i in range(1,len(sys.argv)):
    print(sys.argv[i],end="\n")