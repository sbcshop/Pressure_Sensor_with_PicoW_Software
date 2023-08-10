#Code for testing onboard Display 

from machine import Pin, ADC,SPI
import vga1_bold_16x32 as font
import utime,time
import st7789 #library of TFT display controller uses SPI interface

#define and configure display SPI pins
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
