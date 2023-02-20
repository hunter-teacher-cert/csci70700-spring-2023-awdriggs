# Rail Fence Cipher https://en.wikipedia.org/wiki/Rail_fence_cipher

# encode! 
def encode(message, rails):
    message = message.replace(" ", "") #get rid of the spaces
    scramble = [] #empty list for the encoding

    for i in range(rails):
        scramble.append("") #add an empty string for each rail

    row = 0 #start at row 0 
    dir = -1 #direction to move through the rails, set to -1 since it will get changed to 1 on the edge check
 
    for i in range(len(message)): #loop through the message
        # print(row); #debug the pingpong walk through the fences
        scramble[row] += message[i]
    
        if(row == 0 or row == rails-1): #at an edge, move in opposite direction
            dir *= -1
    
        row += dir
     
    return ' '.join(scramble)
 
def main():
    #get message
    print("Rail Fence Encryption")
    message = input("Type a message to encode: ")

    while True:
        rails = int(input("Number of rails (1 to 8): "))
        if(rails > 0 and rails <= 8 and rails < len(message)):
            break;
        else:
            print("Invalid rails value! Try again!")
    
    encoded_msg = encode(message, rails)
    print(encoded_msg)

if __name__ == "__main__":
    main()
