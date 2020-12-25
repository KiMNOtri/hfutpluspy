import loginfunction
import tkinter


def loginfun():
    
    
    print("Input Username:")
    username = input()
    print("Input Password:")
    passwd = input()

    loginfunction.login(username,passwd)