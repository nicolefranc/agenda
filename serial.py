import serial
import time

members = 6

def connect_with_arduino():  # connects with the arduino by trying out the different ports, then returns the port number
    ports = ["COM3", "COM4", "COM5", "/dev/ttyUSB0", "/dev/ttyUSB1"]
    rate = 9600
    for i in ports:
        try:
            s1 = serial.Serial(i, rate)
            print("Port used: " + i)
            return i
        except:
            print(i + " failed")
            continue
    else:
        print("No ports found. ")
        user_port = input("Manually input port or enter 'n' to exit: ")
        if user_port.upper == 'N':
            try:
                s1 == serial.Serial(user_port, rate)
                print(user_port)
                return (user_port)
            except:
                print("failed")
                input("Press enter to continue: ")

def checkstate(members):
    line = ""
    while True:
        message = str(s1.read())
        message_crop = str(message[2:-1])
        if message_crop !=".":
            line+=message_crop
        elif message_crop ==".":
            if line[-1] =="Activated": # when big button is pressed, agenda item cleared
                print(line)
            if line[-1] =="1":
                n = "1."+str(members)
                s1.write(n.encode('utf-8'))
                print("State Changed")
                return True
            # elif line[-1]=="0": # nothing happens, simply display web page
                n="0."+str(members)
                s1.write(n.encode('utf-8'))
                print(line)
            line = ""

port = connect_with_arduino()
s1 = serial.Serial(port, 9600)

while True:
    checkstate(members)