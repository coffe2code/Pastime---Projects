'''
This code generates a QR code for the required information.
QR codes are merely two-dimensional barcodes that encode
a string that can be parsed by another program. This code
genereates a QR code which encodes the WiFi credentials of
my home network. The credentials are in the form of the 
following string :-

WIFI:S:<SSID>;T:<WPA|WEP|>;P:<password>;;

SSID - Network name
WPA|WEP - Securtiy type
password - Network password

'''

import pyqrcode as pq 

ssid = "IIT(BHU)"
security = "WPA"
password = "yZ^BnLw^yh"


qr = pq.create("WIFI:S:"+ssid+";T:"+security+";P:"+password+";;")

print(qr.terminal()) #This should print the qr code to the terminal
