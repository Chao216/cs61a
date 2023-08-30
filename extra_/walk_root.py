import os
for root,folders,files in os.walk("./"):
    print(root)
    
    print("\n")
    print("--------------------------------------------")
    print("\n")

    for i in root:
        print(i)
    
    print("\n")
    print("--------------------------------------------")
    print("\n")