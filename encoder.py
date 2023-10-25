loop = 1
code = "empty"

def menu():
    global code
    global loop

    print('''Menu
-------------
1. Encode
2. Decode
3. Quit
''')
    option = input("Please enter an option: ")
    match option:
        case "1":
            code = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            print("")
        case "2":
            print("The encoded password is " + code + ", and the original password is " + decode(code) + ".")
            print("")
        case "3":
            loop = 0
        case "_":
            print("Invalid input! Please choose a number between one and three.")
            print("")


def encode(code):
    final = ''

    for i in code:
        if int(i) >= 7: 
            final += str(int(i) - 7)
        else:
            final += str(int(i) + 3)
        
    
    return(final)

def decode(code):
    final = ''
    
    #HERE
    #Make the decoder here.
    #It needs to subtract three from each of the digits of the input, 'code'.
    #If that would make it negative it should loop back around.
    #-1 becomes 9, -2 becomes 8, etc. 

    return(final)