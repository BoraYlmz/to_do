from tkinter import *
import smootwin
import os



class message_box():
    
    global wrong_image,warning_image,checked_image,message_control,os_image,ok_destroy,no_destroy,resp
    resp = StringVar()
    def no_destroy():
        message_frame.destroy()
        resp.set("NO")
    
    def ok_destroy():
        message_frame.destroy()
        resp.set("OK")
    
    wrong_image = PhotoImage(file=os.path.join(os.getcwd(), r"To_Do/icon", "wrong.png"))
    warning_image = PhotoImage(file=os.path.join(os.getcwd(), r"To_Do/icon", "warning.png"))
    checked_image = PhotoImage(file=os.path.join(os.getcwd(), r"To_Do/icon", "checked.png"))
    # os_image=PhotoImage(file="icon/Logo.png")
    
    
    def message_box_create(boxtype,box_name,message,btn):
        global  message_box_x , message_box_y ,message_box_button_panel,message_frame
        
        
        message_box_x=400
        message_box_y=200
        message_frame=Toplevel(smootwin.root)
        screenx=(smootwin.root.winfo_screenwidth()-message_box_x)/2
        screeny=(smootwin.root.winfo_screenheight()-message_box_y)/2
        message_frame.geometry("{0}x{1}+{2}+{3}".format(message_box_x,message_box_y,int(screenx),int(screeny)))
        message_frame.attributes('-topmost','true')
        message_frame.overrideredirect(True)
        message_frame.configure(background=smootwin.DGRAY,highlightbackground=smootwin.BGRAY,highlightthickness=1)
        
        message_box_top_panel=Frame(message_frame,bg=smootwin.DGRAY,highlightthickness=0)
        message_box_top_panel.place(relx=0, rely=0, relwidth=1, relheight=0.125)
        
        message_box_line=Frame(message_frame,bg=smootwin.BGRAY,highlightthickness=1,highlightbackground=smootwin.BGRAY)
        message_box_line.place(relx=0, rely=0.126, relwidth=1, relheight=0.001)
        
        message_box_bottom_panel=Frame(message_frame,bg=smootwin.DGRAY,highlightthickness=0)
        message_box_bottom_panel.place(relx=0, rely=0.13, relwidth=1, relheight=0.7)
        
        message_box_button_panel=Frame(message_frame,bg=smootwin.DGRAY,highlightthickness=0)
        message_box_button_panel.place(relx=0, rely=0.83, relwidth=1, relheight=0.17)
        
        
        if boxtype == "wrong":
            title_bar_icon=Label(message_box_bottom_panel,image=warning_image,bg=smootwin.RGRAY,bd=0,highlightthickness=0)
            title_bar_icon.pack(side=LEFT, padx=10)
        elif boxtype == "warning":
            title_bar_icon=Label(message_box_bottom_panel,image=warning_image,bg=smootwin.RGRAY,bd=0,highlightthickness=0)
            title_bar_icon.pack(side=LEFT, padx=10)   
        elif boxtype == "ok":
            title_bar_icon=Label(message_box_bottom_panel,image=checked_image,bg=smootwin.RGRAY,bd=0,highlightthickness=0)
            title_bar_icon.pack(side=LEFT, padx=10)  
        # title_bar_icon=Label(message_box_top_panel,image=os_image,bg=smootwin.RGRAY,bd=0,highlightthickness=0)
        # title_bar_icon.pack(side=LEFT, padx=10)
        message_box_title = Label(message_box_top_panel, text=box_name, bg=smootwin.RGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),highlightthickness=0)
        message_box_title.pack(side=LEFT, padx=0)
        message_box_message=Label(message_box_bottom_panel, text=message_control(message), bg=smootwin.RGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),highlightthickness=0)
        message_box_message.pack(side=LEFT, padx=0)
        
        if(btn == "OK"):
            ok_btn= Button(message_box_button_panel,text="TAMAM",fg="white",bg="#ca1217",font=("calibri", 11,"bold"),highlightthickness=0,bd=0,activebackground="red",command=ok_destroy)
            ok_btn.place(relx=0.5,rely=0.5,anchor=CENTER,relheight=0.75,relwidth=0.2)
        elif btn == "NO":
            no_btn= Button(message_box_button_panel,text="HAYIR",fg="white",bg="#ca1217",font=("calibri", 11,"bold"),highlightthickness=0,bd=0,activebackground="red",command=no_destroy)
            no_btn.place(relx=0.5,rely=0.5,anchor=CENTER,relheight=0.75,relwidth=0.2)
        elif (btn == "OKNO"):
            ok_btn= Button(message_box_button_panel,text="TAMAM",fg="white",bg="#ca1217",font=("calibri", 11,"bold"),highlightthickness=0,bd=0,activebackground="red",command=ok_destroy)
            ok_btn.place(relx=0.35,rely=0.5,anchor=CENTER,relheight=0.75,relwidth=0.2)
            no_btn= Button(message_box_button_panel,text="HAYIR",fg="white",bg="#ca1217",font=("calibri", 11,"bold"),highlightthickness=0,bd=0,activebackground="red",command=no_destroy)
            no_btn.place(relx=0.65,rely=0.5,anchor=CENTER,relheight=0.75,relwidth=0.2)
        
        message_frame.grab_set()
        smootwin.root.wait_variable(resp) 
        return resp.get()
        
    
    
     
    def message_control(message):
        message_len = (message_box_x -50)/10
        for i in range(len(message)):
            if int(i+1)%int(message_len) == 0:
                message = message[:i]+'\n'+message[i:]
        
        return message
    
    
    
    
    
    
    