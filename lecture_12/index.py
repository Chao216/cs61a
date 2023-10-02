# index takes a sequence of keys, a sequence of values, and a function that takes 2 args,, if match, return a dictionary

def index(keys,values,match):
    dict1={} # create empty dictionary
    for i in keys:# loop through keys sequence
        val_list = [] # create empty val list
        for j in values: # loop through values sequence
            if match(i,j): # if returns true
                val_list.append(j) 
        dict1[i] = val_list # add key, value_list pair to the empty dictionary
    return dict1
print(index(range(1,10),range(1,100),lambda x,y:y%x==0))

dic_test = index(range(1,10),range(1,100),lambda x,y:y%x==0)

for i,j in zip(dic_test.keys(),dic_test.values()):
    print(i,"\t===>\t",j)
