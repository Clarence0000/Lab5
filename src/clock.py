import time 
import hal.hal_lcd as lcd

lcd = lcd.lcd()
lcd.lcd_clear()

def main():
    while(True):
        local_time = time.localtime() # get struct_time
        time_hour = time.strftime("%H", local_time) 
        time_min= time.strftime("%M", local_time)
        time_sec = time.strftime("%S", local_time)
        time_day = time.strftime("%d", local_time) 
        time_month = time.strftime("%m", local_time)
        time_year = time.strftime("%Y", local_time)


        current_time = time_hour + " : " + time_min + " : " + time_sec
        current_date = time_day + " : " + time_month + " : " + time_year

        lcd.lcd_display_string(current_time, 1)
        lcd.lcd_display_string(current_date, 2)

        time.sleep(1)
        
        local_time = time.localtime() # get struct_time
        time_hour = time.strftime("%H", local_time) 
        time_min= time.strftime("%M", local_time)
        time_sec = time.strftime("%S", local_time)
        time_day = time.strftime("%d", local_time) 
        time_month = time.strftime("%m", local_time)
        time_year = time.strftime("%Y", local_time)
        
        current_time = time_hour + "   " + time_min + "   " + time_sec
        current_date = time_day + "   " + time_month + "   " + time_year

        lcd.lcd_display_string(current_time, 1)
        lcd.lcd_display_string(current_date, 2)

        time.sleep(1)


if __name__ == "__main__":
    main()