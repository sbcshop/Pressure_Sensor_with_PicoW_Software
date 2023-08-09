#Code for combine testing pressure sensor, Display, Joystick and buzzer

from machine import Pin, ADC,SPI
import vga1_bold_16x32 as font
import utime,time
import st7789 #library of TFT display controller uses SPI interface

buzz = Pin(15,Pin.OUT) # up
buzz.value(0)
joy_up = Pin(16,Pin.IN, Pin.PULL_UP) # up
joy_left  = Pin(17,Pin.IN, Pin.PULL_UP) # left
joy_down   = Pin(18,Pin.IN, Pin.PULL_UP) # down
joy_right  = Pin(19,Pin.IN, Pin.PULL_UP) # right
joy_centre    = Pin(20,Pin.IN, Pin.PULL_UP) # centre

potentiometer_value = machine.ADC(26)

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)#SPI interface for tft screen

def main():
    tft.init()
    time.sleep(0.5)#time delay
   
    tft.text(font,"SB COMPONENTS", 10,40,st7789.YELLOW)# print on tft screen
    tft.fill_rect(0, 72, 240,10, st7789.RED)#display red line on tft screen
    
    tft.text(font,"PICO PRESSURE", 10,120,st7789.GREEN)
    tft.fill_rect(0, 152, 240,10, st7789.RED)
    
    time.sleep(1)
    tft.fill(0)
    
main()
    
while(True):
        potreading = potentiometer_value.read_u16()
        tft.text(font,"PRESSURE", 55,40,st7789.YELLOW)# print on tft screen
        tft.fill_rect(0, 72, 240,10, st7789.BLUE)#display red line on tft screen
        tft.text(font,str(potreading), 20,120,st7789.GREEN)
        print("potADC: ",potreading)
        utime.sleep(0.1)
        
        
        if(joy_up.value() == 0):
            buzz.value(1)
            print("joy_up press")
            tft.fill(0x0fff)     #0x00ff for red color 
                  
        elif(joy_left.value() == 0):
            buzz.value(1)
            print("joy_left press")
            tft.fill(0x0f00)     #0x00ff for blue color 

        elif(joy_down.value() == 0):
            buzz.value(1)
            print("joy_down press")
            tft.fill(0xf00f)      #0x00ff for green color 
            
        elif(joy_right.value() == 0):
            buzz.value(1)
            print("joy_right press")
            tft.fill(0x00ff)      #0x00ff for yellow color 
       
        elif(joy_centre.value() == 0):
            buzz.value(1)
            print("joy_centre press")
            tft.fill(0xfff0)      #0x00ff for pink color
            
            
        else:
            buzz.value(0)
        time.sleep(0.2)
        
        
