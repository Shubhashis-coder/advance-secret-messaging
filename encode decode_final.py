# import tkinter module 
from tkinter import *

# import other necessery modules 
import random 
import time 
import datetime 
def mainpage(q):
        try:
                q.destroy()
        except:
                pass
# creating root object 
        root = Tk() 

# defining size of window 
        root.geometry("12000x6000") 

# setting up the title of window 
        root.title("Message Encryption and Decryption") 
        logo = PhotoImage(file="11 (2).png")
        logo_final= Label(root,image=logo,bg='#FFFFFF',fg = "Blue").place(x=0,y=0)
        lblInfo = Label(root, font = ('algerian', 50), 
		text = "SECRET MESSAGING \n SHUBHASHIS MONDAL", 
					fg = "red",bg='black' ,bd = 10, anchor='w') 
        lblInfo.place(x= 400, y= 0) 
        rand = StringVar() 
        Msg = StringVar() 
        key = StringVar() 
        mode = StringVar() 
        Result = StringVar() 

        # exit function 
        def qExit(): 
                root.destroy() 

        # Function to reset the window 
        def Reset(): 
                rand.set("") 
                Msg.set("") 
                key.set("") 
                mode.set("") 
                Result.set("") 


        # reference 
        lblReference = Label(root, font = ('arial', 16, 'bold'), 
                                        text = "Name:", bd = 16, anchor = "w") 
                                        
        lblReference.place(x = 0, y =240) 

        txtReference = Entry(root, font = ('arial', 16, 'bold'), 
                                textvariable = rand, bd = 10, insertwidth = 4, 
                                                        bg = "powder blue", justify = 'right') 
                                                        
        txtReference.place(x = 150, y =240) 

        # labels 
        lblMsg = Label(root, font = ('arial', 16, 'bold'), 
                        text = "MESSAGE", bd = 16, anchor = "w") 
                        
        lblMsg.place(x = 0, y = 340) 

        txtMsg = Entry(root, font = ('arial', 26, 'bold'), 
                        textvariable = Msg, bd = 10, insertwidth = 4, 
                                        bg = "powder blue", justify = 'right') 
                                        
        txtMsg.place(x = 150, y =340) 

        lblkey = Label(root, font = ('arial', 20, 'bold'), 
                                text = "KEY", bd = 16, anchor = "w") 
                                
        lblkey.place(x = 600, y = 440) 

        txtkey = Entry(root, font = ('arial', 16, 'bold'), 
                        textvariable = key, bd = 10, insertwidth = 4, 
                                        bg = "powder blue", justify = 'right') 
                                        
        txtkey.place(x = 780, y =445) 

        lblmode = Label(root, font = ('arial', 16, 'bold'), 
                        text = "MODE(e for encrypt, d for decrypt)", 
                                                                        bd = 16, anchor = "w") 
                                                                        
        lblmode.place(x = 0, y = 445) 

        txtmode = Entry(root, font = ('arial', 10, 'bold'), 
                        textvariable = mode, bd = 10, insertwidth = 4, 
                                        bg = "powder blue", justify = 'right') 
                                                
        txtmode.place(x = 400, y = 450) 

        lblService = Label(root, font = ('arial', 16, 'bold'), 
                                text = "The \n Result-", bd = 16, anchor = "w") 
                                
        lblService.place(x = 0, y = 550) 

        txtService = Entry(root, font = ('arial', 60, 'bold'), 
                                textvariable = Result, bd = 10, insertwidth = 4, 
                                                bg = "powder blue", justify = 'right') 
                                                        
        txtService.place(x =150, y = 510) 

        # Vigenère cipher 
        import base64 

        # Function to encode 
        def encode(key, clear): 
                enc = [] 
                
                for i in range(len(clear)): 
                        key_c = key[i % len(key)] 
                        enc_c = chr((ord(clear[i]) +
                                                ord(key_c)) % 256) 
                                                
                        enc.append(enc_c) 
                        
                return base64.urlsafe_b64encode("".join(enc).encode()).decode() 

        # Function to decode 
        def decode(key, enc): 
                dec = [] 
                
                enc = base64.urlsafe_b64decode(enc).decode() 
                for i in range(len(enc)): 
                        key_c = key[i % len(key)] 
                        dec_c = chr((256 + ord(enc[i]) -
                                                        ord(key_c)) % 256) 
                                                                
                        dec.append(dec_c) 
                return "".join(dec) 


        def Ref(): 
                print("Message= ", (Msg.get())) 

                clear = Msg.get() 
                k = key.get() 
                m = mode.get() 

                if (m == 'e'): 
                        Result.set(encode(k, clear)) 
                else: 
                        Result.set(decode(k, clear)) 

        # Show message button 
        btnTotal = Button(root, padx = 16, pady = 8, bd = 16, fg = "black", 
                                                        font = ('arial', 16, 'bold'), width = 10, 
                                                text = "Show Message", bg = "powder blue", 
                                                        command = Ref).place(x =200, y =650) 

        # Reset button 
        btnReset = Button(root, padx = 16, pady = 8, bd = 16, 
                                        fg = "black", font = ('arial', 16, 'bold'), 
                                                width = 10, text = "Reset", bg = "green", 
                                        command = Reset).place(x = 700, y = 650) 

        # Exit button 
        btnExit = Button(root, padx = 16, pady = 8, bd = 16, 
                                        fg = "black", font = ('arial', 10, 'bold'), 
                                                width = 5, text = "Exit", bg = "red", 
                                        command = qExit).place(x = 1430, y = 0) 

        # keeps window alive 
        root.mainloop() 
mainpage('')
