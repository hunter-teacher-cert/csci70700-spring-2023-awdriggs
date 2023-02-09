import random

def stupid():
    return "hello stupid"

def get_seed(r):
    seed = "" #build a seed
    
    if r: #random seed string
        for i in range(49):
            if random.random() > 0.5:
                seed = seed + "1"
            else:
                seed = seed + "0"
    else: 
    #seed string for a middle black square
        for i in range(49):
            if i == 24: #middle value
                seed = seed + "1"
            else:
                seed = seed + "0"

    return seed
 
def automate(seed_str, sets, rules):
    row = ""
    print(len(seed_str))
    #loop through each letter in the place string
    for i in range(len(seed_str)):
        value = "";

        #look at the at my neightbors, ugh edges
        if i > 0 and i < len(seed_str)-1:
            #i'm not at the edge if my place is > 0 and is < len
            value = seed_str[i-1] + seed_str[i] + seed_str[i+1]
        elif i == 0:
            #add a 0 to the beginning
            value = "0" + seed_str[i] + seed_str[i+1]
        else:
            value = seed_str[i-1] + seed_str[i] + "0"
        # print("value " + value)
        # print("{:d}".format(i) + " " + seed_str[i])
         
        index = rules.index(value) #match current value to a value in the rules list, store the index

        #get the value from that index from the sets list
        #this is the new value to give the row.
        row += sets[index]  

    return row #ready for next iteration

def get_set(num):
    return list("{:08b}".format(num)) #list of the binary representation of the rule set number as a sring
 
def build(number, random_seed):
    board = []
    rules = ["111", "110", "101", "100", "011", "010", "001", "000"] #the rules
    setrule = get_set(number)
    seed = get_seed(random_seed)

    for i in range(50):
        board.append(seed)
        seed = automate(seed, setrule, rules)

    return board 
