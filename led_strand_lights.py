# Imports
import board
from neopixel import NeoPixel
import time

# LED details
LEDcount = 15

# Define the strand pin number and number of LEDs from variables
strand = NeoPixel(board.D21, LEDcount)

# Colour variables
red = 64,0,0
green = 0,64,0

# LED index list
ledindex = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Turn off all LEDs before program start
strand.fill((0,0,0))
strand.write()
time.sleep(1)

while True:
    
    # First loop runs red evens and green odds
    for led in ledindex:
        
        if (led % 2) == 0: #If the LED index is even
            strand[led] = (red)
                
        else: # If not (odd numbers)
            strand[led] = (green)
        
        strand.write()
    
    # Delay to show the colours before changing them
    time.sleep(1)
    
    # Second loop runs green evens and red odds
    for led in ledindex:
        
        if (led % 2) == 0: #If the LED index is even
            strand[led] = (green)
                
        else: # If not (odd numbers)
            strand[led] = (red)
        
        strand.write()

    # Delay to show the colours before changing them    
    time.sleep(1)

