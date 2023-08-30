import os
for root,folders,files in os.walk("./"):
    print(folders)
    print("\n")
    print("--------------------------------------------")
    print("\n")
    for dir in folders:
        print(dir)
    
    print("\n")
    print("--------------------------------------------")
    print("\n")