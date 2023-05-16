# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial

def main:
    # Configure the serial port
    ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with your actual port name
    ser.timeout = 1  # Set a timeout value (in seconds) to wait for data

    # Read and respond to data
    while True:
        data = ser.readline().decode().strip()  # Read a line of data from the serial port
        if data:
            print("Received data:", data)
            response = "Response to '{}'".format(data)  # Generate a response based on the received data
            ser.write(response.encode())  # Send the response back through the serial port

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
