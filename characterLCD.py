import RPi.GPIO as GPIO
import time
 
# Define GPIO to LCD mapping
registerPin = 15
enablePin  = 23
pin4 = 27
pin5 = 22
pin6 = 10
pin7 = 9
 
# Define some device constants
screenWidth = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
 
line1 = 0x80 # LCD RAM address for the 1st line
line2 = 0xC0 # LCD RAM address for the 2nd line
 
# Timing constants
enableDelay = 0.0005
 
def main():
  # Main program block
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)

  GPIO.setup(enablePin, GPIO.OUT)
  GPIO.setup(registerPin, GPIO.OUT)
  GPIO.setup(pin4, GPIO.OUT)
  GPIO.setup(pin5, GPIO.OUT)
  GPIO.setup(pin6, GPIO.OUT)
  GPIO.setup(pin7, GPIO.OUT)
 
  while True:
    #use lcdString() to write to lcd
 
    lcdString("Penis", line1)
    time.sleep(3)
 
    lcdString("Double", line1)
    lcdString("Penis", line2)
    time.sleep(3)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command
 
  GPIO.output(registerPin, mode) # RS
 
  # High bits
  GPIO.output(pin4, False)
  GPIO.output(pin5, False)
  GPIO.output(pin6, False)
  GPIO.output(pin7, False)
  if bits&0x10==0x10:
    GPIO.output(pin4, True)
  if bits&0x20==0x20:
    GPIO.output(pin5, True)
  if bits&0x40==0x40:
    GPIO.output(pin6, True)
  if bits&0x80==0x80:
    GPIO.output(pin7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
  # Low bits
  GPIO.output(pin4, False)
  GPIO.output(pin5, False)
  GPIO.output(pin6, False)
  GPIO.output(pin7, False)
  if bits&0x01==0x01:
    GPIO.output(pin4, True)
  if bits&0x02==0x02:
    GPIO.output(pin5, True)
  if bits&0x04==0x04:
    GPIO.output(pin6, True)
  if bits&0x08==0x08:
    GPIO.output(pin7, True)
 
  # Toggle 'Enable' pin
  lcd_toggle_enable()
 
def lcd_toggle_enable():
  # Toggle enable
  time.sleep(enableDelay)
  GPIO.output(enablePin, True)
  time.sleep(enableDelay)
  GPIO.output(enablePin, False)
  time.sleep(enableDelay)
 
def lcdString(message,line):
  # Send string to display
 
  message = message.ljust(screenWidth)
 
  lcd_byte(line, LCD_CMD)
 
  for i in range(screenWidth):
    lcd_byte(ord(message[i]),LCD_CHR)
 
if __name__ == '__main__':
 
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcdString("Goodbye!",line1)
    GPIO.cleanup()
