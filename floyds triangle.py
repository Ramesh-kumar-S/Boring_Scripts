rows=input("Enter Rows: ")
No=int(1)
for i in range(int(rows)+1):
    for j in range(i):
        print(No,end =' ')
        No += 1
    print(end='\n')