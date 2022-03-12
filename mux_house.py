import time 

def AND(a,b):
    if ((a == b) and a == 1):
        return True
    else:
        return False

def OR(a,b):
    if (a == 1 or b == 1):
        return True
    else:
        return False

def XOR(a,b):
    if ((a == 1 or b == 1) and (a != b)):
        return True
    else:
        return False

def print_menu():
    print("Please choose the following options and wake up a logic droid [S0, S1, S2]: ")
    print("0. Do nothing: [0,0,0]")
    print("1. AND: [0,0,1]")
    print("2. NAND: [0,1,0]")
    print("3. OR: [0,1,1]")
    print("4. NOR: [1,0,0]")
    print("5. XOR: [1,0,1]")
    print("6. XNOR: [1,1,0]")
    print("7. NOT for I1: [1,1,1]")
    return 0


# all will be in a while True loop
#### Inputs ####
sel_hold = [0,0,0,0]    # 4 elements [S2, S1, S0, Hold], switches
in_button = [0,0]       # 2 elements, [I1, I0], buttons

# sel_hold = [1,1,1]
# in_button = [0,1]
print("*********Welcome to the MUX House!!*********")

try:
    while True:
        print_menu()        # print menu of MUX House
        sel_hold[0] = int(input("Enter S0: "))
        sel_hold[1] = int(input("Enter S1: "))
        sel_hold[2] = int(input("Enter S2: "))
        sel_hold[3] = int(input("Hold? [0/no, 1/yes]: "))
        
        in_button[1] = int(input("Enter I1: "))
        in_button[0] = int(input("Enter I0: "))

        print("You chose for sel_hold = [" + str(sel_hold[3]) + "," + str(sel_hold[2]) + "," + str(sel_hold[1]) + "," + str(sel_hold[0]) + "]\n")
        print("You chose for in_button = [" + str(sel_hold[1]) + "," + str(sel_hold[0]) + "]\n")
        
        if (sel_hold[0:3] == [0,0,0]):      # in the order of [S0, S1, S2]
            # do nothing
            print("do nothing")
            result = 0
        elif (sel_hold[0:3] == [0,0,1]):
            # AND operation
            print("AND")
            result = AND(in_button[0],in_button[1])
        elif (sel_hold[0:3] == [0,1,0]):
            # NAND operation
            print("NAND")
        elif (sel_hold[0:3] == [0,1,1]):
            # OR operation
            print("OR")
            result = OR(in_button[0],in_button[1])
        elif (sel_hold[0:3] == [1,0,0]):
            # NOR operation
            print("NOR")
            result = OR(in_button[0],in_button[1])
            result = not result
        elif (sel_hold[0:3] == [1,0,1]):
            # XOR operation
            print("XOR")
            result = XOR(in_button[0],in_button[1])
        elif (sel_hold[0:3] == [1,1,0]):        
            # XNOR operation
            print("XNOR")
            result = XOR(in_button[0],in_button[1])
            result = not result
        else:   # sel[0:3] == [1,1,1]
            # NOT operation
            print("NOT")
            result = not in_button[1]

        print(result)
        while (sel_hold[3] == 1):
            # hold result, user can change logic but must stay here
            time.sleep(5)
            sel_hold[3] = 0
except KeyboardInterrupt:
    pass

print("Goodbye!")