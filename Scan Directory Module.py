import os
with os.scandir("/home/ramesh") as it:
    for entry in it:
        if entry.is_file():
            
            print(entry.name)