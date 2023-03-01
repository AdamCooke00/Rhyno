from pyezviz import *
import time

#Setting account login info and the serial number of the camera to be used
#Note this account info should probably be kept in a .env file.. I have removed the password for pushing to git
email = "*******"
password = "*******"
serial = "*******"

#Client to login to ezviz - username and password are account info for logging into ezviz account
client =  EzvizClient(email,password,"apiius.ezvizlife.com")

#EzViz Camera object using the valid client and specifying the serial number of the camera (SN is on physical camera)
camera = EzvizCamera(client,serial)

def ctrlLeft(cmd):
    client.ptz_control(str("left").upper(), serial, cmd.upper(), 2)

def ctrlRight(cmd):
    client.ptz_control(str("right").upper(), serial, cmd.upper(), 2)


def ctrlUp(cmd):
    client.ptz_control(str("up").upper(), serial, cmd.upper(), 2)


def ctrlDown(cmd):
    client.ptz_control(str("down").upper(), serial, cmd.upper(), 2)
