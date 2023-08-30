import os
for root,folders,files in os.walk("./"):
    print(files)
    print("\n")
    print("------------------------------------------")
    print("\n")

    for name in files:
        print(name)
    
    print("\n")
    print("------------------------------------------")
    print("\n")