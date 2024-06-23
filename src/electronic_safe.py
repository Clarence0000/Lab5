from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD

password = []

lcd = LCD.lcd()
lcd.lcd_clear()

def key_pressed(key):
    global password
    password.append(key)

    print(password)

def out_thread():
    global password
    outputstr = ""
    rightOrWrong = 0
    
    while(True):
        while(rightOrWrong != -1):
            
            if len(password) > 0:       #clear second row
                print("cleared")
                lcd.lcd_clear()
                lcd.lcd_display_string("Safe Lock", 1)
            

            while(len(password) > 0 and rightOrWrong != -1):

                while(len(outputstr) < len(password)):          #REQ02
                    outputstr += "*"
                    lcd.lcd_display_string("Safe Lock", 1) 
                    lcd.lcd_display_string(outputstr, 2)    
                    
                if len(password) == 4 and rightOrWrong < 3:
                    if password == [1,2,3,4]:                    #REQ03
                        print("correct")
                        rightOrWrong = -1

                    else:                                       #REQ04
                        print("wrong")
                        outputstr = ""
                        password = []
                        
                        rightOrWrong += 1
                        lcd.lcd_clear()
                        lcd.lcd_display_string("Wrong PIN", 1)

            if rightOrWrong == 3:                   #REQ05
                print("disabled")
                lcd.lcd_clear()
                while(True):
                    lcd.lcd_display_string("Safe Disabled", 1)    

            elif rightOrWrong == -1:                #REQ03
                lcd.lcd_clear()
                lcd.lcd_display_string("Safe Unlocked", 1)
                lcd.lcd_display_string("", 2)

        while(rightOrWrong == -1):
            if '*' in password:         #lock safe
                outputstr = ""
                rightOrWrong = 0
                password = []
                
                print("lock")

                lcd.lcd_display_string("Safe Lock      ", 1)
                lcd.lcd_display_string("Enter PIN:", 2)




def main():
    lcd = LCD.lcd()
    lcd.lcd_clear()

    lcd.lcd_display_string("Safe Lock", 1)
    lcd.lcd_display_string("Enter PIN:", 2)

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()

    threat_out = Thread(target=out_thread)
    threat_out.start()


if __name__ == "__main__":
    main()