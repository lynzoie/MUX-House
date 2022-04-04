from machine import Pin
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

def toggle_pin(LED, value):
    while (LED.value() != value):
        LED.toggle()
    
    return 0

############ SETUP ALL I/O PINS ############
# Input Buttons
I0_btn = Pin(27, Pin.IN, Pin.PULL_DOWN)
I1_btn = Pin(26, Pin.IN, Pin.PULL_DOWN)

# DIP Switches
DIP_Switch_1 = Pin(18, Pin.IN, Pin.PULL_DOWN)
DIP_Switch_2 = Pin(19, Pin.IN, Pin.PULL_DOWN)
DIP_Switch_3 = Pin(20, Pin.IN, Pin.PULL_DOWN)
DIP_Switch_4 = Pin(21, Pin.IN, Pin.PULL_DOWN)

# RGB Pins
R_Pin = Pin(2, Pin.OUT)
G_Pin = Pin(1, Pin.OUT)
B_Pin = Pin(0, Pin.OUT)

# LED Pins
LED_1 = Pin(15, Pin.OUT)
LED_2 = Pin(14, Pin.OUT)
LED_3 = Pin(13, Pin.OUT)
LED_4 = Pin(12, Pin.OUT)
LED_5 = Pin(11, Pin.OUT)
LED_6 = Pin(10, Pin.OUT)
LED_7 = Pin(9, Pin.OUT)

# Input LEDs
I1_LED = Pin(7, Pin.OUT)
I0_LED = Pin(8, Pin.OUT)

# all will be in a while True loop
#### Inputs ####
sel_hold = [0,0,0,0]    # 4 elements [S2, S1, S0, Hold], switches
in_button = [0,0]       # 2 elements, [I1, I0], buttons

# sel_hold = [1,1,1]
# in_button = [0,1]
print("*********Welcome to the MUX House!!*********")

# Turn off all LEDs before running program
#toggle_pin(I1_LED,0)
#toggle_pin(I0_LED,0)

#toggle_pin(LED_1,0)
#toggle_pin(LED_2,0)
#toggle_pin(LED_3,0)
#toggle_pin(LED_4,0)
#toggle_pin(LED_5,0)
#toggle_pin(LED_6,0)
#toggle_pin(LED_7,0)

#toggle_pin(R_Pin,0)
#toggle_pin(G_Pin,0)
#toggle_pin(B_Pin,0)
try:
    while True:
        #print_menu()        # print menu of MUX House
        sel_hold = [DIP_Switch_1.value(), DIP_Switch_2.value(), DIP_Switch_3.value(), DIP_Switch_4.value()]
        
        in_button[1] = I1_btn.value()
        in_button[0] = I0_btn.value()

        print("You chose for sel_hold = [" + str(sel_hold[0]) + "," + str(sel_hold[1]) + "," + str(sel_hold[2]) + "," + str(sel_hold[3]) + "]\n")
        print("You chose for in_button = [" + str(in_button[1]) + "," + str(in_button[0]) + "]\n")

        # output Input LEDs
        if in_button[1]:
            toggle_pin(I1_LED,1)
        else:
            toggle_pin(I1_LED,0)

        if in_button[0]:
            toggle_pin(I0_LED,1)
        else:
            toggle_pin(I0_LED,0)
        
        time.sleep(0.1)
        if (sel_hold[0:3] == [0,0,0]):      # in the order of [S0, S1, S2]
            # do nothing
            print("do nothing")
            toggle_pin(LED_1,0)
            toggle_pin(LED_2,0)
            toggle_pin(LED_3,0)
            toggle_pin(LED_4,0)
            toggle_pin(LED_5,0)
            toggle_pin(LED_6,0)
            toggle_pin(LED_7,0)
            result = -1
        elif (sel_hold[0:3] == [0,0,1]):
            # AND operation
            print("AND")
            result = AND(in_button[0],in_button[1])
            toggle_pin(LED_1,1)
            toggle_pin(LED_2,0)
            toggle_pin(LED_3,0)
            toggle_pin(LED_4,0)
            toggle_pin(LED_5,0)
            toggle_pin(LED_6,0)
            toggle_pin(LED_7,0)
        elif (sel_hold[0:3] == [0,1,0]):
            # NAND operation
            print("NAND")
            result = AND(in_button[0],in_button[1])
            result = not result
            toggle_pin(LED_1,0)
            toggle_pin(LED_2,1)
            toggle_pin(LED_3,0)
            toggle_pin(LED_4,0)
            toggle_pin(LED_5,0)
            toggle_pin(LED_6,0)
            toggle_pin(LED_7,0)
        elif (sel_hold[0:3] == [0,1,1]):
            # OR operation
            print("OR")
            toggle_pin(LED_1,0)
            toggle_pin(LED_2,0)
            toggle_pin(LED_3,1)
            toggle_pin(LED_4,0)
            toggle_pin(LED_5,0)
            toggle_pin(LED_6,0)
            toggle_pin(LED_7,0)
            result = OR(in_button[0],in_button[1])
        elif (sel_hold[0:3] == [1,0,0]):
            # NOR operation
            print("NOR")
            toggle_pin(LED_1,0)
            toggle_pin(LED_2,0)
            toggle_pin(LED_3,0)
            toggle_pin(LED_4,1)
            toggle_pin(LED_5,0)
            toggle_pin(LED_6,0)
            toggle_pin(LED_7,0)
            result = OR(in_button[0],in_button[1])
            result = not result
        elif (sel_hold[0:3] == [1,0,1]):
            # XOR operation
            print("XOR")
            toggle_pin(LED_1,0)
            toggle_pin(LED_2,0)
            toggle_pin(LED_3,0)
            toggle_pin(LED_4,0)
            toggle_pin(LED_5,1)
            toggle_pin(LED_6,0)
            toggle_pin(LED_7,0)
            result = XOR(in_button[0],in_button[1])
        elif (sel_hold[0:3] == [1,1,0]):        
            # XNOR operation
            print("XNOR")
            result = XOR(in_button[0],in_button[1])
            result = not result
            toggle_pin(LED_1,0)
            toggle_pin(LED_2,0)
            toggle_pin(LED_3,0)
            toggle_pin(LED_4,0)
            toggle_pin(LED_5,0)
            toggle_pin(LED_6,1)
            toggle_pin(LED_7,0)
        else:   # sel[0:3] == [1,1,1]
            # NOT operation
            print("NOT")
            result = not in_button[1]
            toggle_pin(LED_1,0)
            toggle_pin(LED_2,0)
            toggle_pin(LED_3,0)
            toggle_pin(LED_4,0)
            toggle_pin(LED_5,0)
            toggle_pin(LED_6,0)
            toggle_pin(LED_7,1)

        print(result)
        if (result == -1):
            toggle_pin(R_Pin,0)
            toggle_pin(G_Pin,0)
            toggle_pin(B_Pin,0)
        elif (result == 1):
            toggle_pin(R_Pin,0)
            toggle_pin(G_Pin,1)
            toggle_pin(B_Pin,0)
        else:
            toggle_pin(R_Pin,1)
            toggle_pin(G_Pin,0)
            toggle_pin(B_Pin,0)
        while (DIP_Switch_4.value()):
            # hold result, user can change logic but must stay here
            time.sleep(1)
            

except KeyboardInterrupt:
    pass

print("Goodbye!")

