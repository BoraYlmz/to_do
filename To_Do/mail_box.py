import smootwin
import cripto as cp
from tkinter import *
from tkinter import ttk
import messagebox as mbox
import os
from tinydb import TinyDB, Query
# from new_mail_win import new_mail_win
import new_mail_win
from scroll_frame import VerticalScrolledFrame
import json


class boxes(object):
    def __init__(self, user_id: int):
        self.user_id = user_id
    
    def new_mail_open(self):
        open_window =new_mail_win.new_mail_win_open(self.user_id)
        box_id =open_window.new_mail()
        #create_box(self,mail_id,menu_id,header,owner,delete_button)
        db_query = Query()
        box_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "box_inf.json"))
        box_table_result = box_table.get(db_query.id == int(box_id))
        user_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
        user_table_result = user_table.get(db_query.id == int(box_table_result['owner_id']))
        self.create_box(int(box_id),box_table_result['parent'],box_table_result['header'],user_table_result['name'],True,box_table_result['level'])
        user_table.close()
        box_table.close()
        
    
    def panels(self):
        new_mail = Button(smootwin.root, text='   +   ', command=self.new_mail_open,bg=smootwin.DGRAY,font=("calibri", 15),bd=0,fg='white',highlightthickness=0,activeforeground=smootwin.RGRAY)
        new_mail.place(relx=0.999,y=36,anchor=NE)
        new_mail.bind("<Enter>", self.on_enter_bg)
        new_mail.bind("<Leave>", self.on_leave_bg)
        framex=round((1-0.03)/3.0,2) 
        self.beginning_frame =  Frame(smootwin.root,bg=smootwin.PGRAY,highlightbackground=smootwin.BGRAY,highlightthickness=1)#soldaki kutu
        self.beginning_frame.place(relx=0.01, rely=0.1, relwidth=framex, relheight=0.89)
        self.beginning_inner_frame = VerticalScrolledFrame(self.beginning_frame)#soldaki kutunun scrolu
        self.beginning_inner_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        
        self.progress_frame =  Frame(smootwin.root,bg=smootwin.PGRAY,highlightbackground=smootwin.BGRAY,highlightthickness=1)#ortadaki kutu
        self.progress_frame.place(relx=framex+0.02, rely=0.1, relwidth=framex, relheight=0.89)
        self.progress_inner_frame = VerticalScrolledFrame(self.progress_frame)#ortadaki kutunun scrolu
        self.progress_inner_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.ending_frame =  Frame(smootwin.root,bg=smootwin.PGRAY,highlightbackground=smootwin.BGRAY,highlightthickness=1)#sağdaki kutu
        self.ending_frame.place(relx=framex*2+0.03, rely=0.1, relwidth=framex, relheight=0.89)
        self.ending_inner_frame = VerticalScrolledFrame(self.ending_frame)#sağdaki kutunun scrolu
        self.ending_inner_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        user_box_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "user_box.json"))
        box_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "box_inf.json"))
        user_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
        # veritabanlarına bağlanıp sorgu çalıştırıyor çıkan sorguları(kutu id, kutu_id,başlığı,kimin gönderdiği) createbox fonksitonuna gönderiyor 
        # Bunlar kişinin mail kutusunu oluşturmaktadır.
        db_query = Query()
        user_box_result = user_box_table.search(db_query.user_id == self.user_id)
        for item in user_box_result:
            box_id = int(item["box_id"])
            box_table_result = box_table.get(db_query.id == box_id)
            delete_button = False
            if box_table_result["owner_id"] == self.user_id:
                delete_button= True
            user_table_result = user_table.get(db_query.id == box_table_result["owner_id"])
            boxes.create_box(self,box_table_result["id"],box_table_result["parent"],box_table_result["header"],user_table_result["name"],delete_button,box_table_result["level"])
        
        user_box_table.close()
        box_table.close()
        user_table.close()

    def create_box(self,mail_id,menu_id,header,owner,delete_button,level): # mail kutullarını oluşturan fonksiyon
        parent=0
        if menu_id == 1:
            parent= self.beginning_inner_frame.interior
        elif menu_id == 2:
            parent= self.progress_inner_frame.interior
        elif menu_id == 3:
            parent= self.ending_inner_frame.interior 
        box_x=(int(smootwin.root.winfo_screenwidth())*0.97)/3
        box=Frame(parent,bg=smootwin.PGRAY,highlightbackground=smootwin.BGRAY,highlightthickness=1,width=box_x,height=65,name=str(mail_id))
        box.pack(side=TOP,padx=5,pady=5)
        
        box_header = Label(box,bg=smootwin.PGRAY,text=header,fg='white',font=("calibri", 11,"bold"),highlightthickness=0)
        box_header.place(relx=0,rely=0,anchor=NW)
        box_owner = Label(box,bg=smootwin.PGRAY,text=owner,fg='white',font=("calibri", 11,"bold"),highlightthickness=0)
        box_owner.place(relx=1,rely=1,anchor=SE)
        if level == 1:
            box_level = Label(box,bg=smootwin.PGRAY,text= "↓",fg='aqua',font=("calibri", 13,"bold"),highlightthickness=0)
            box_level.place(relx=0.1,rely=0.55,anchor=E)
        elif level == 2:
            box_level = Label(box,bg=smootwin.PGRAY,text= " =  ",fg='green',font=("calibri", 14,"bold"),highlightthickness=0)
            box_level.place(relx=0.12,rely=0.5,anchor=E)
        elif level == 3:
            box_level = Label(box,bg=smootwin.PGRAY,text= "↑",fg='red',font=("calibri", 13,"bold"),highlightthickness=0)
            box_level.place(relx=0.1,rely=0.55,anchor=E)
        box.bind("<1>",self.on_click)
        if delete_button:
            del_icon=Button(box,bg=smootwin.PGRAY,text="♲",font=("bold",15),fg="white",activebackground=smootwin.DGRAY,border=0,bd=0)
            del_icon.place(relx=1,rely=0,anchor=NE)
            del_icon.bind("<1>",self.delete_mail)
            del_icon.bind("<Enter>", self.on_enter)
            del_icon.bind("<Leave>", self.on_leave)
    
    def delete_mail(self,event):
        resp = mbox.message_box.message_box_create("wrong","Emin Misiniz?","Maddeyi silmek istediğinize emin misiniz?","OKNO")
        if resp == "OK":
            mail_id = int(smootwin.root.nametowidget(event.widget.winfo_parent()).winfo_name())
            user_box=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "user_box.json"))
            query = Query()
            user_box.remove(query.box_id == mail_id)
            user_box.close()
            box_db=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "box_inf.json"))
            box_db.remove(query.id == mail_id)
            box_db.close()
            if os.path.exists(os.path.join(os.getcwd(), r"To_Do/data/comment", "{0}_comment.json").format(mail_id)):
                os.remove(os.path.join(os.getcwd(), r"To_Do/data/comment", "{0}_comment.json").format(mail_id))
                smootwin.root.nametowidget(event.widget.winfo_parent()).destroy()
       
        
    # Mail kutusuna tıklandığında mail id çeker ve uygulama ortasına bir pencere açar    
    def on_click(self, event): 
        self.box_id = int(event.widget.winfo_name())
        message_body_frame=Toplevel(smootwin.root,bg=smootwin.DGRAY)
        
        self.x_widht  = int(smootwin.root.winfo_width()*0.9)
        x_center = int(smootwin.root.winfo_x())+int(smootwin.root.winfo_width()*0.05)
        y_height = int(smootwin.root.winfo_height()*0.9)
        y_center = int(smootwin.root.winfo_y())+int(smootwin.root.winfo_height()*0.075)
        
        message_body_frame.geometry("{}x{}+{}+{}".format(self.x_widht,y_height,x_center, y_center)) #mesaj penceresi
        message_body_frame.overrideredirect(True)
        message_body_frame.grab_set()
        
        message_body_top_frame =Frame(message_body_frame,bg=smootwin.DGRAY,highlightthickness=1,highlightbackground=smootwin.BGRAY) # mesaj kutusunun iç frame
        message_body_top_frame.place(relx=0.5,rely=0.05,relwidth=1,relheight=0.049,anchor=N)
        
        style = ttk.Style()
        style.configure("TCombobox",arrowsize=22, foreground="white",font=("calibri", 13), background=smootwin.DGRAY,darkcolor=smootwin.DGRAY,bordercolor=smootwin.BGRAY,borderwidth=1,arrowcolor="white",lightcolor=smootwin.DGRAY)
        style.map("TCombobox",fieldbackground=[('readonly',smootwin.DGRAY)])
        style.map("TCombobox",selectbackground=[('readonly',smootwin.DGRAY)])
        
        self.mail_level_var= StringVar()
        self.mail_level = ttk.Combobox(message_body_top_frame,style="TCombobox",textvariable=self.mail_level_var,state="readonly")
        self.mail_level.place(relx=1,rely=0.5,relwidth=0.3,anchor=E)
        
        self.mail_level['values']=('Başlamadı','Yapımda','Bitti')
        
        box_db=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "box_inf.json"))
        db_query = Query()
        box_db_result = box_db.get(db_query.id == self.box_id)
        
        if box_db_result['parent'] == 1:
            self.mail_level.set('Başlamadı')
        elif box_db_result['parent'] == 2:
            self.mail_level.set('Yapımda')
        elif box_db_result['parent'] == 3:
            self.mail_level.set('Bitti')
        
        self.mail_level.bind('<<ComboboxSelected>>',self.parent_change)
        
        message_body_bottom_frame =Frame(message_body_frame,bg=smootwin.DGRAY,highlightthickness=1,highlightbackground=smootwin.BGRAY) # mesaj kutusunun iç frame
        message_body_bottom_frame.place(relx=0.5,rely=1,relwidth=1,relheight=0.9,anchor=S)
        
        self.message_body_inner_frame = VerticalScrolledFrame(message_body_bottom_frame) #iç frame kutusunu kaydırılabilir yapar
        self.message_body_inner_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        toolbar=Frame(message_body_frame,bg=smootwin.DGRAY,highlightthickness=1,highlightbackground=smootwin.BGRAY,relief='raised') 
        toolbar.pack(fill=X)
        
        close_button = Button(toolbar, text='  ×  ', command=message_body_frame.destroy,bg=smootwin.RGRAY,padx=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0,activeforeground=smootwin.RGRAY)
        close_button.pack(side=RIGHT,ipadx=7,ipady=1)
        close_button.bind("<Enter>", self.on_enter_bg)
        close_button.bind("<Leave>", self.on_leave_bg)
        
        # self.icon_iamge=PhotoImage(file="icon/logo.png")
        # self.toolbar_icon=Label(toolbar,image=self.icon_iamge,bg=smootwin.RGRAY,bd=0,highlightthickness=0)
        # self.toolbar_icon.pack(side=LEFT,padx=10)
        
        toolbar_title = Label(toolbar, bg=smootwin.RGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),highlightthickness=0)
        toolbar_title.pack(side=LEFT,padx=0)
        
        # mail içi yazışmaları çeker ve açılan pencereye oluşturur
        box_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "box_inf.json"))
        db_query = Query()
        box_table_result = box_table.get(db_query.id == self.box_id)
        toolbar_title.configure(text=box_table_result['header'])
        
        box_text = TinyDB(os.path.join(os.getcwd(), r"To_Do/data/comment", "{0}_comment.json").format(self.box_id))
        # box_text_result = box_text.search(db_query.box_id == self.box_id)
        
        user_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
        for item in box_text:
            user_result = user_table.get(db_query.id == item["user_id"])
            self.box_create(user_result['name'],item['Text'])
        box_text.close()
        user_table.close()
        box_table.close()
        self.main_content()
        # self.new_comment()
    
    def parent_change(self,event):
        box_db=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "box_inf.json"))
        db_query = Query()
        box_db_result = box_db.get(db_query.id == self.box_id)
        if box_db_result['parent'] == 1:
            self.beginning_inner_frame.interior.nametowidget(self.box_id).destroy()
        elif box_db_result['parent'] == 2:
            self.progress_inner_frame.interior.nametowidget(self.box_id).destroy()
        elif box_db_result['parent'] == 3:
            self.ending_inner_frame.interior.nametowidget(self.box_id).destroy()
                               
        if self.mail_level_var.get() == 'Başlamadı':
            box_db.update({'parent':1},Query().id==self.box_id)
        elif self.mail_level_var.get() == 'Yapımda':
            box_db.update({'parent':2},Query().id==self.box_id)
        elif self.mail_level_var.get() == 'Bitti':
            box_db.update({'parent':3},Query().id==self.box_id)
        
        delete_button = False
        if box_db_result["owner_id"] == self.user_id:
            delete_button= True
        box_db_result = box_db.get(db_query.id == self.box_id)
        user_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
        user_table_result = user_table.get(db_query.id == box_db_result["owner_id"])
        boxes.create_box(self,box_db_result["id"],box_db_result["parent"],box_db_result["header"],user_table_result["name"],delete_button,box_db_result["level"])
        box_db.close()
        user_table.close()
    
    
    def comment_key_press(self,event):
        hg = int(event.widget.index('end').split('.')[0])-1
        parent = self.message_body_inner_frame.interior.nametowidget(event.widget.winfo_parent())
        parent.config(height=80+(hg*17))
        event.widget.place(height=40+(hg*17))

    def new_comment(self): # yeni yorum kutusu oluşturur.
        comment_box = Frame(self.message_body_inner_frame.interior,bg=smootwin.DGRAY,highlightthickness=1,highlightbackground=smootwin.BGRAY,height=80)
        comment_box.pack(side=BOTTOM,fill=X,padx=10,pady=5)
        
        comment_box_new_Text = Text(comment_box,bg=smootwin.DGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),highlightbackground=smootwin.BGRAY,highlightthickness=1,height=17)
        comment_box_new_Text.place(relx=0.01,rely=0.01,anchor=NW,relwidth=0.98,height=40)
        comment_box_new_Text.bind("<KeyPress>", self.comment_key_press)
        
        comment_box_btn=Button(comment_box,bg=smootwin.DGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),text="Gönder",justify="left",activebackground="red",activeforeground="white",border=0.5)
        comment_box_btn.place(relx=0.99,rely=0.99,anchor=SE)
        comment_box_btn.bind("<1>",self.comment_button)
        
        
    def comment_button(self,event): #gönder tuşuna basıldığında yorumu alır kutu olarak ekler ve yeni yorum kutusu oluşturur
        user_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
        comment_data=TinyDB(os.path.join(os.getcwd(), r"To_Do/data/comment", "{0}_comment.json").format(self.box_id))
        last_comment_id = comment_data.get(doc_id=len(comment_data))
        db_query = Query()
        user_result = user_table.get(db_query.id == self.user_id)
        child = smootwin.root.nametowidget(event.widget.winfo_parent()).winfo_children()
        for item in child:
            try:
                new_comment = ({    "id":int(last_comment_id['id']+1),
                                "user_id":self.user_id,
                                "Text":item.get("1.0",'end-1c')})
            except:
                new_comment = ({    "id":1,
                                "user_id":self.user_id,
                                "Text":item.get("1.0",'end-1c')})
            comment_data.insert(new_comment)
            comment_data.close()
            self.box_create(user_result['name'],item.get("1.0",'end-1c'))
            break
        comm_child=[]
        comment_box_parent = smootwin.root.nametowidget(event.widget.winfo_parent())
        for item in self.message_body_inner_frame.interior.winfo_children():
            comm_child.append(item)
        smootwin.root.nametowidget(comm_child[-2]).destroy()
        comment_box_parent.destroy()
        self.main_content()
        
        
    
    def box_create(self,user_name,text): # Yorum kutularına oluşturma fonksiyonu
        
        text = self.message_control(text)
        hg = text.count("\n")
        hg = 75 +((hg+1)*17)
        comment_box = Frame(self.message_body_inner_frame.interior,bg=smootwin.DGRAY,highlightthickness=1,highlightbackground=smootwin.BGRAY,height=hg)
        comment_box.pack(side=BOTTOM,fill=X,padx=10,pady=5)
        
        comment_box_user_name = Label(comment_box,bg=smootwin.DGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),text=user_name,pady=0)
        comment_box_user_name.pack(anchor="w",side=TOP)
        
        comment_box_text=Label(comment_box,bg=smootwin.DGRAY,bd=0,fg='white',font=("calibri", 11,"bold"),text=text,justify="left",pady=25)
        comment_box_text.pack(anchor="w",side=TOP)   
        
    def message_control(self,text):# Mesaj içeriğini ekran genişliğine göre yapılandırma fonksiyonu
        
        satır_uzunluk = int((self.x_widht)/7.5)
        text_len = len(text)
        message_len = satır_uzunluk
        alt_index=0
        before_len=0
        while message_len < text_len:#2. satır \n ifadesini görmüyor
            before_len=message_len
            lng= text[alt_index:message_len].find("\n")
            if lng < 1:
                text = text[:message_len]+"\n"+text[message_len:]
                alt_index += satır_uzunluk 
                message_len+=satır_uzunluk
            else:
                alt_index +=lng
                message_len +=lng
            if before_len ==  message_len:
                break
                  
        return text
        
    def main_content(self):
        self.new_comment()
        box_table=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "box_inf.json"))
        db_query = Query()
        box_table_result = box_table.get(db_query.id == self.box_id)
        user_table = TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
        user_table_result = user_table.get(db_query.id == box_table_result['owner_id'])
        self.box_create(user_table_result['name'],box_table_result['content'])      
        
    def on_enter_bg(self,event):
        event.widget.configure(background="red")

    def on_leave_bg(self,event):
        event.widget.configure(background=smootwin.RGRAY)    
        
    def on_enter(self,event):
        event.widget.configure(foreground="#cc0000")

    def on_leave(self,event):
        event.widget.configure(foreground="white")
    
    
    