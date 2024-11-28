from tinydb import TinyDB, Query
from tkinter import *
from tkinter import ttk
import messagebox as mbox
import smootwin
import mail_box
from scroll_frame import VerticalScrolledFrame
import os


class new_mail_win_open(object):
    def __init__(self, user_id: int):
        self.user_id = user_id
        
    def on_enter_bg(self,event):
        event.widget.configure(background="red")

    def on_leave_bg(self,event):
        event.widget.configure(background=smootwin.RGRAY)  
        
    def new_mail(self):
        self.new_mail_window=Toplevel(smootwin.root,bg=smootwin.DGRAY,highlightbackground=smootwin.BGRAY,highlightthickness=1)
        
        self.x_widht  = int(smootwin.root.winfo_width()*0.9)
        x_center = int(smootwin.root.winfo_x())+int(smootwin.root.winfo_width()*0.05)
        y_height = int(smootwin.root.winfo_height()*0.9)
        y_center = int(smootwin.root.winfo_y())+int(smootwin.root.winfo_height()*0.075)
        
        self.new_mail_window.geometry("{}x{}+{}+{}".format(self.x_widht,y_height,x_center, y_center)) #mesaj penceresi
        self.new_mail_window.overrideredirect(True)
        self.new_mail_window.grab_set()
        
        toolbar=Frame(self.new_mail_window,bg=smootwin.DGRAY,highlightthickness=1,highlightbackground=smootwin.BGRAY,relief='raised') 
        toolbar.pack(fill=X)
        
        close_button = Button(toolbar, text='  ×  ', command=self.new_mail_window.destroy,bg=smootwin.RGRAY,padx=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0,activeforeground=smootwin.RGRAY)
        close_button.pack(side=RIGHT,ipadx=7,ipady=1)
        close_button.bind("<Enter>", self.on_enter_bg)
        close_button.bind("<Leave>", self.on_leave_bg)
        
        # self.icon_iamge=PhotoImage(file="icon/logo.png")
        # self.toolbar_icon=Label(toolbar,image=self.icon_iamge,bg=smootwin.RGRAY,bd=0,highlightthickness=0)
        # self.toolbar_icon.pack(side=LEFT,padx=10)
        
        toolbar_title = Label(toolbar, bg=smootwin.RGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),highlightthickness=0,text="New Mail")
        toolbar_title.pack(side=LEFT,padx=0)
        
        self.new_mail_header = Entry(self.new_mail_window,bg=smootwin.DGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),highlightbackground=smootwin.BGRAY,highlightthickness=1)
        self.new_mail_header.place(relx=0.5,y=40,anchor=N,height=25,relwidth=0.8)
        
        self.content_box = Text(self.new_mail_window,bg=smootwin.DGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),highlightbackground=smootwin.BGRAY,highlightthickness=1)
        self.content_box.place(relx=0.5,y=70,anchor=N,relheight=0.5,relwidth=0.8)
        
        style = ttk.Style()
        style.configure("TCombobox",arrowsize=22, foreground="white",font=("calibri", 13), background=smootwin.DGRAY,darkcolor=smootwin.DGRAY,bordercolor=smootwin.BGRAY,borderwidth=1,arrowcolor="white",lightcolor=smootwin.DGRAY)
        style.map("TCombobox",fieldbackground=[('readonly',smootwin.DGRAY)])
        style.map("TCombobox",selectbackground=[('readonly',smootwin.DGRAY)])
        user_list ={}
        users=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
        for i in users:
            user_list[i['id']] = i['mail']
        
        # mail_to_var= StringVar()
        self.mail_to_var=""
        self.mail_to = Entry(self.new_mail_window,bg=smootwin.DGRAY,bd=0,highlightbackground=smootwin.BGRAY,highlightthickness=1,font=("calibri", 13),fg="white")
        self.mail_to.place(relx=0.1,rely=0.65,relwidth=0.3)
        self.mail_to.bind("<FocusIn>",self.dropdown_menu)
        self.mail_to.bind("<FocusOut>",self.dropdown_menu_destroy)
        
        self.mail_level_var= StringVar()
        self.mail_level = ttk.Combobox(self.new_mail_window,style="TCombobox",textvariable=self.mail_level_var,state="readonly")
        self.mail_level.place(relx=0.6,rely=0.65,relwidth=0.3)
        
        self.mail_level['values']=('High','Normal','Low')
        
        
        
        self.box_datas=StringVar()
        self.create_mail_btn=Button(self.new_mail_window,command=self.new_mail_create,bg=smootwin.DGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),text="Oluştur",justify="left",activebackground="red",activeforeground="white",border=0.5)
        self.create_mail_btn.place(relx=0.5,rely=0.75,anchor=CENTER)   
        smootwin.root.wait_variable(self.box_datas)
        return self.box_datas.get()
        
    def new_mail_create(self):
        if self.new_mail_header.get() == " " or self.new_mail_header.get() == "" :
            mbox.message_box.message_box_create("wrong","Boş Metin Hatası!","Mail Başlığını Kontrol Ediniz!!","OK")
        else:
            if self.mail_to_var == "":
                mbox.message_box.message_box_create("wrong","Gönderim Hatası!","Gönderilecek Kişi Seçiniz!!","OK")
            else:
                if self.mail_level.get() == "":
                    mbox.message_box.message_box_create("wrong","Seviye Hatası","Mail Önceliğini Belirleyiniz!!","OK")
                else:
                    box_table = TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "box_inf.json"))
                    result = box_table.all()[-1]#box_table.get(doc_id=len(box_table))

                    level =0
                    if self.mail_level.get() == "High":
                        level=3
                    elif self.mail_level.get() == "Normal":
                        level=2
                    else:
                        level=1

                    box_inf_data = ({   "id":int(result['id'])+1,
                                        "level":level,
                                        "owner_id":self.user_id,
                                        "header":self.new_mail_header.get(),
                                        "parent":1,
                                        "owner_box_id":int(result['id'])+1,
                                        "content":self.content_box.get("1.0",'end-1c')})
                    user_box_table = TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "user_box.json"))
                    result2 = user_box_table.all()[-1]#user_box_table.get(doc_id=len(user_box_table))
                    user_box_data = ({   "id":int(result2['id'])+1,
                                        "user_id":self.user_id,
                                        "box_id":int(result['id'])+1
                                        })
                    user_box_table.insert(user_box_data)
                    
                    user_table = TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
                    db_query = Query()
                    result2 = user_box_table.all()[-1]
                    user_box_table_result = user_table.get(db_query.mail == self.mail_to_var)
                    
                    user_box_data = ({   "id":int(result2['id'])+1,
                                        "user_id":int(user_box_table_result['id']),
                                        "box_id":int(result['id'])+1
                                        })
                    user_box_table.insert(user_box_data)
                    user_box_table_result = user_table.get(db_query.id == self.user_id)
                    mail_box_class = mail_box.boxes(self.user_id)
                    user_table.close()
                    user_box_table.close()
                    box_table.insert(box_inf_data)
                    box_table.close()
                    self.box_datas.set(int(result['id'])+1)
                    #create_box(self,mail_id,menu_id,header,owner,delete_button)
                    self.new_mail_window.destroy()
                    
    def dropdown_menu(self,event):
        window=smootwin.root.nametowidget(event.widget.winfo_parent())
        menu=Frame(window,bg=smootwin.DGRAY,bd=0,highlightbackground=smootwin.BGRAY,height=200,highlightthickness=1,name=str(event.widget.winfo_name())+"_dropdown")
        menu.place(x=event.widget.winfo_x(),y=event.widget.winfo_y()+25,width=event.widget.winfo_width())
        menu_scrol = VerticalScrolledFrame(menu)
        menu_scrol.place(relx=0, rely=0, relwidth=1, relheight=1)
        user_list={}
        users=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
        for i in users:
            user_list[i['mail']] = i['name']
        
        for i in user_list:
            userbox=Frame(menu_scrol.interior,bg=smootwin.DGRAY,bd=0,highlightbackground=smootwin.BGRAY,height=50,width=event.widget.winfo_width()-20,highlightthickness=1,name=i)
            userbox.pack(side=BOTTOM,pady=5)
            userbox.bind("<1>",self.click_to_userbox)
        
            userbox_name = Label(userbox,bg=smootwin.DGRAY,text=user_list[i],bd=0,font=("calibri", 11,"bold"),fg="white")
            userbox_name.place(relx=0,rely=0,anchor=NW)
        
            userbox_mail = Label(userbox,bg=smootwin.DGRAY,text=i,bd=0,font=("calibri", 8,"bold"),fg="white")
            userbox_mail.place(relx=0,rely=1,anchor=SW)
    
    def click_to_userbox(self,event): # mail gönderirken kişi seçildiğinde
        for item in event.widget.winfo_children():
            self.mail_to.delete(0,END)
            self.mail_to.insert(0,item.cget('text'))
            self.mail_to_var = event.widget.winfo_name()    
            break     
        box_list = self.new_mail_window.nametowidget(event.widget.winfo_parent()) # kaydırılabilir menü için içe içe frame kullanıldı Budan dolayı 
        box_list2 = self.new_mail_window.nametowidget(box_list.winfo_parent())  # kişi şeçildiğinde en üstteki kutuyu bulmak için dosyada geri gidiyoruz.
        box_list3 =self.new_mail_window.nametowidget(box_list2.winfo_parent())
        self.new_mail_window.nametowidget(box_list3.winfo_parent()).destroy() # en üst kutuya gelince dropdown kapatıyoruz.
    
    def dropdown_menu_destroy(self,event):
        try:
            self.new_mail_window.nametowidget(str(event.widget.winfo_name())+"_dropdown").destroy()
        except:
            None