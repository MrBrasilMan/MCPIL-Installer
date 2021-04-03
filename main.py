from tkinter import *
import tkinter
import tkinter.messagebox as msgbox
import os
import requests
import subprocess
quick_message = "Thanks for using my custom MCPI Launcher\ninstaller!\n\nThis program is made for easy \ninstallation of the MCPI Launcher.\n\nClick the install button below\nto install the launcher into the current\nworking directory"
#git clone --recurse-submodules https://github.com/MCPI-Revival/MCPIL.git\ncd MCPIL\n./scripts/package.sh
def messager():
  if os.system("git clone --recurse-submodules https://github.com/MCPI-Revival/MCPIL.git\ncd MCPIL\n./scripts/package.sh") == 0:
    msgbox.showinfo("Yay!", "The installer has ran with no issues")
    if os.system("python MCPIL/src/launcher.py") == 0:
      pass
    else:
      msgbox.showerror("Snap!", "Can't self boot launcher.")
  else:
    dodiag = msgbox.askquestion("Snap!", "The installation failed. Run diagonstics?")
    if dodiag == "yes":
      found_error = False
      try:
        requests.get("http://www.example.com")
      except:
        msgbox.showinfo("Possible Error Found.", "You need to connect to the internet to install the launcher")
        found_error = True
      if os.system("git --version") != 0:
        msgbox.showinfo("Possible Error Found.", "Git is required for installation.")
        found_error = True
      if os.system("cd MCPIL\ncd scripts\n") != 0:
         msgbox.showinfo("Possible Error Found.", "Cannot find location for MCPI to run.\nAre you not root?")
         found_error = True
      if os.system("cd /usr/bin/minecraft-pi") != 0:
         msgbox.showinfo("Possible Error Found.", "Cannot find a valid Minecraft Pi install.")        
      if found_error == False:
        msgbox.showerror("Snap!", "Diagnostic Failed.")
root = Tk()
root.title("MCPI Launcher Installer")
root.geometry('335x190')


starttext = Text(root, height=9, width=40)
button = Button(text = "Install", height = 1, width = 10, command = messager)
starttext.insert('1.0', quick_message)

starttext.place(x=0, y=0)
button.place(x=100, y=160)
root.mainloop()