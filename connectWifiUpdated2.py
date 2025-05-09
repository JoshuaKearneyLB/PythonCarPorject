#import sys

import network
import socket
from time import sleep

ssid = "****"
password = '*******'

def webpage():
    html = """
    
    <!DOCTYPE html>
    <html>
    <body>
    <form action= "./lighton">
    <input type = "submit" value = "light on " />
    </form>
    </body>
    </html>
    
    
    """

def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())
    ip = wlan.ifconfig()[0]
    print('Connected to:', ip)
    return ip


# creating a socket so the server can listen for client requests
def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(3 )
    print(connection)
    # socket state = 1 means the socket is open and working
    return connection

def serve(connection):
    
    #creating webpage
    while 1:
        print("inside while loop")
        client = connection.accept()[0]
        request = client.recv (1024)
        request = str(request)
        print(request)

            #to add more functionality from the website add more if statments and get the response from the website to see what the user wants to do
            #need the car to finnish and test it
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == "/close":
            sys.exit()

        #if request == "/lights on"
            # lights.on (example)
            #saveToDataBase(request:-1) remove the backslash from the request


        print(request)
        client.close

        #will not work as the webpage source code needs to be copied into webpage()

        html = webpage()
        client.send(html)







ip = connect()
print("part 1")
connection = open_socket(ip)
print("part 2")
serve(connection)
print("part 3")
