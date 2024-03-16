import os

cmd = ""

while (cmd != "exit"):
    cmd = input("enter your command: ")
    print(os.popen(cmd,'r').read())
