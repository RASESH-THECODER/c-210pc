#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

name=None
listbox=None
textarea=None
labelchat=None
text_message=None

def connecttoserver():
    global SERVER
    global name
    global sending_file
    cname=name.get()
    SERVER.send(cname.encode())

def musicWindow():
    from tkinter import filedialog
    window=Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    selectLabel = Label(window,text="Select Song",bg='LightSkyBlue',font=("Calibri",8))
    selectLabel.place(x=2,y=1)

    listbox=Listbox(window,height=10,width=39,activestyle='dotbox',bg='LightSkyBlue',borderwidth=2,font=("Calibri",10))
    scrollbar1=Scrollbar(listbox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listbox.yview)

    PlayButton=Button(window,text="Play",width=10,bd=1,bg='skyBlue',font=("Calibri",10))
    PlayButton.place(x=30,y=200)

    Stop=Button(window,text="Play",width=10,bd=1,bg='SkyBlue',font=("Calibri",10))
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Upload",width=10,bd=1,bg=('SkyBlue'),font=("Calibri",10))
    Upload.place(x=30,y=250)

    Download=Button(window,text="Download",width=10,bd=1,bg='SkyBlue',font=("Calibri",10))
    Download.place(x=200,y=250)

    infoLabel=Label(window,text="",fg="blue",font=("Calibri",8))
    infoLabel.place(x=4,y=280)

    window.mainloop()
# def openChatWindow():

#     print("\n\t\t\t\tIP MESSENGER")
#     window=Tk()
#     window.title("messenger")
#     window.geometry("500x500")
#     global name
#     global listbox
#     global textarea
#     global labelchat
#     global text_message
#     global filepathlabel
#     namelabel=Label(window,text="enter your name",font=("Calibri",10))
#     namelabel.place(x=10,y=8)


#     name=Entry(window,width=30,font=("Calibri",10))
#     name.place(x=120,y=8)

#     connectserver=Button(window,bd=1,text="connect to chat server",font=("Calibri",10),command=connecttoserver)
#     connectserver.place(x=350,y=6)

#     seperator=ttk.Separator(window,orient="horizontal")
#     seperator.place(x=0,y=35,relwidth=1,height=0.9)
#     labelusers=Label(window,text="active users",font=("Calibri",10))
#     labelusers.place(x=10,y=50)

#     listbox=Listbox(window,activestyle="dotbox",height=5,width=67,font=("Calibri",10))
#     listbox.place(x=10,y=70)

#     scrollbar1=Scrollbar(listbox)
#     scrollbar1.place(relheight=1,relx=1)
#     scrollbar1.config(command=listbox.yview)

#     connectButton=Button(window,text="connect",bd=1,font=("Calibri",10))
#     connectButton.place(x=282,y=160)

#     disconnectButton=Button(window,text="disconnect",bd=1,font=("Calibri",10))
#     disconnectButton.place(x=350,y=160)

#     refresh=Button(window,text="refresh",bd=1,font=("Calibri",10))
#     refresh.place(x=435,y=160)

#     labelchat=Label(window,text="chat window",bd=1,font=("Calibri",10))
#     labelchat.place(x=10,y=180)

#     textarea=Text(window,width=67,height=6,bd=1,font=("Calibri",10))
#     textarea.place(x=10,y=200)

#     scrollbar2=Scrollbar(textarea)
#     scrollbar2.place(relheight=1,relx=1)
#     scrollbar2.config(command=listbox.yview)

#     attach=Button(window,text="attach and send",bd=1,font=("Calibri",10))
#     attach.place(x=10,y=305)

#     text_message=Entry(window,width=43,bd=1,font=("Calibri",12))
#     text_message.place(x=98,y=306)

#     send=Button(window,text="send",bd=1,font=("Calibri",10))
#     send.place(x=450,y=305)

#     filepathlabel=Label(window,text="",fg="cyan",bd=1,font=("Calibri",10))
#     filepathlabel.place(x=10,y=330)
#     window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    musicWindow()

setup()


#-----------Bolierplate Code Start -----

