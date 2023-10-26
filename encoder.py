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
    length = len(str(code))
    num = int
    while length != 0:
        num = (int(str(code)[0:1])) - 3
        if num < 0:
            num = 10 + num
        final = final + str(num)
        code = str(code)[1:]
        length -= 1
    return final



def main():
    global loop
    while loop == 1:
        menu()


if __name__ == "__main__":
    main()