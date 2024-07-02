import RPi.GPIO as GPIO
import time
import serial
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT) #RS 485 Enable Pin
# Serial Port Settings
rs_485_ser = serial.Serial(
    port='/dev/ttyS0',  # Raspberry Pi's serial port's name
    baudrate=9600,      # Connection Speed (Baudrate)
    timeout=1           # Timeout Settings
)
#RS485 Data
data = bytes([0x01, 0x03, 0x00, 0x00, 0x00, 0x04, 0x44, 0x09]) # Total active energy
try:
    GPIO.output(33, GPIO.HIGH)
    rs_485_ser.write(data)
    time.sleep(0.01)  
    GPIO.output(33, GPIO.LOW)
    rs_485_ser.reset_output_buffer()
    rs_485_ser.reset_input_buffer()
    response = rs_485_ser.readline()
    if response:                       
        byte_array = bytearray(response)  #Response is coming byte by byte, so we have to convert to array to compare datas
        byte_list = list(byte_array)
        print("Response :")
        for i in range (len(byte_list)):
            print (i+1,". byte is = ",byte_list[i])

except Exception as e:
    print("RS485 an error occurred:", e)
