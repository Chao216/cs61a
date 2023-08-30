import os
for root,folders,files in os.walk("./"):
    print(root)
    print("\n")
    for fod in folders:
       print(fod)
    print("\n")
    for entity in files:
        print(entity)
    print("\n")