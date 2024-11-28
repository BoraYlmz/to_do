
import smootwin
import cripto as cp
from tkinter import *
import messagebox as mbox
import os
from mail_box import boxes
from tinydb import TinyDB, Query
     
                
#-------------------------Login Başlangıç------------------
class login_panel(object):
    
    def reg_panel():
        None
    
    def log_in(self):
        if self.mail_textbox.get().find(" ")>=0:
            mbox.message_box.message_box_create("wrong","Kullanıcı Hatası!","Mail Adresinde Boşluk Olamaz!!","OK")
            self.mail_textbox.configure(highlightcolor='red')
        else:
            user_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
            db_query = Query()
            result = user_table.get(db_query.mail == str(self.mail_textbox.get()))
            if str(result) == "None":
                mbox.message_box.message_box_create("wrong","Kullanıcı Hatası!","Böyle Bir Kullanıcı Bulunamadı!!!","OK")
                self.mail_textbox.configure(highlightcolor='red')
            else:   
                if str(result['passwd']) == str(cp.cripto(self.password.get())):
                    if self.remember_me_var.get() == 1:
                        if os.path.exists(os.path.join(os.getcwd(), r"To_Do/data", "usersetting.cfg")):
                            file = open(os.path.join(os.getcwd(), r"To_Do/data", "usersetting.cfg"),"r+",encoding="utf-8")
                            new_lines=list(file.readlines())
                            new_lines[0] = "remember_me : {0}".format(str(result['id']))
                            file.seek(0)
                            for line in new_lines:
                                file.write(f"{line}\n")
                            file.close()
                        else:
                            f= open(os.path.join(os.getcwd(), r"To_Do/data", "usersetting.cfg"),"w",encoding="utf-8")
                            f.write("remember_me : {0}".format(str(result['id'])))
                            f.close()
                    page = boxes(int(result['id']))
                    page.panels()
                    self.login_win.destroy()
                else:
                    mbox.message_box.message_box_create("wrong","Kullanıcı Hatası!","Şifrenizi Kontrol Ediniz!!!","OK")
                    self.password.configure(highlightcolor='red')

                      
    
    def space_control(self,event):
        txt = event.widget.get()
        if txt.find(" ") >= 0:
            event.widget.configure(highlightcolor='red')
        else:
            event.widget.configure(highlightcolor=smootwin.BGRAY)
            
    def mail_on_entry_click(self,event):
        if self.mail_textbox.get() == "Mail...":
            self.mail_textbox.delete(0, END)
            self.mail_textbox.configure(foreground="white")

    def mail_on_focus_out(self,event):
        if self.mail_textbox.get() == "":
            self.mail_textbox.insert(0, "Mail...")
            self.mail_textbox.configure(foreground="gray")
            
    def pass_on_entry_click(self,event):
        if self.password.get() == "Password...":
            self.password.delete(0, END)
            self.password.configure(foreground="white",show='●')

    def pass_on_focus_out(self,event):
        if self.password.get() == "":
            self.password.insert(0, "Password...")
            self.password.configure(foreground="gray",show='')        
    
    def login_panel_elements(self):
        loginwin_x=0.5
        login_win_y=0.3
        
        screenx=(1-loginwin_x)/2
        screeny=(1-login_win_y)/2
        
                
                
        self.login_win=Frame(bg=smootwin.PGRAY,highlightbackground=smootwin.BGRAY,highlightthickness=1)
        self.login_win.place(relx=screenx, rely=screeny, relwidth=loginwin_x, relheight=login_win_y)#relx=0.275,rely=0.35

        self.mail_textbox=Entry(self.login_win,bg=smootwin.DGRAY,fg='gray',font=('arial',10,'bold'),border=0,highlightthickness=1,highlightbackground=smootwin.BGRAY)
        self.mail_textbox.insert(0, "Mail...")
        self.mail_textbox.place(relx=0.1,rely=0.15,relheight=0.1,relwidth=0.8)
        self.mail_textbox.bind("<Key>",self.space_control)
        self.mail_textbox.bind("<FocusIn>", self.mail_on_entry_click)
        self.mail_textbox.bind("<FocusOut>", self.mail_on_focus_out)

        self.password=Entry(self.login_win,bg=smootwin.DGRAY,fg='gray',font=('arial',10,'bold'),border=0,highlightthickness=1,highlightbackground=smootwin.BGRAY)
        self.password.insert(0, "Password...")
        self.password.place(relx=0.1,rely=0.35,relheight=0.1,relwidth=0.8)
        self.password.bind("<FocusIn>", self.pass_on_entry_click)
        self.password.bind("<FocusOut>", self.pass_on_focus_out)


        self.remember_me_var=IntVar()
        self.remember_me=Checkbutton(self.login_win,fg='white',bg=smootwin.PGRAY,activebackground=smootwin.PGRAY,activeforeground='white',border=0,highlightthickness=0,text='Remember Me',variable=self.remember_me_var,onvalue=1,offvalue=0,selectcolor=smootwin.PGRAY)
        self.remember_me.place(relx=0.1,rely=0.55)

        self.login_button = Button(self.login_win,text='LOGIN',font=('arial',12,'bold'),border=0,foreground='white',bg=smootwin.DGRAY,activebackground='red',activeforeground='white',command=self.log_in)
        self.login_button.place(relx=0.44,rely=0.65)

        # self.register_btn = Button(self.login_win,text='REGISTER',font=('arial',12,'bold'),border=0,foreground='white',bg=smootwin.DGRAY,activebackground='red',activeforeground='white',command=self.reg_panel)
        # self.register_btn.place(relx=0.4,rely=0.85)
        # Kayıt sekmesi eklenecekti fakat bizim tanımladığımız kişiler sisteme girsin gibi bir düşünceye vardık






    
            
#-------------------------Login Bitiş-----------------------