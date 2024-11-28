import smootwin
from tkinter import *
import os
from login import login_panel 
import messagebox as mbox
from mail_box import boxes
from tinydb import TinyDB, Query


# LGRAY = '#3e4042' # button color effects in the title bar (Hex color)
# DGRAY = '#181818' # window background color               (Hex color)
# RGRAY = '#181818' # title bar color                       (Hex color)
# BGRAY = '#353535' # Border color
# PGRAY ='#1f1f1f'

smootwin.root.geometry('800x800')
smootwin.root.minsize(800,800)
smootwin.root.option_add('*TCombobox*Listbox.background', smootwin.DGRAY)
        # # ttk.option_add('*TCombobox*Listbox.font', font)
smootwin.root.option_add('*TCombobox*Listbox.foreground', "white")
smootwin.root.option_add('*TCombobox*Listbox.selectBackground', "red")
smootwin.root.option_add('*TCombobox*Listbox.selectForeground', "white")
# def reg_user():
#     if mail_textbox.get().find(" ")>=0:
#         None
#     else:
#         df_table={"id":[],"mail":[],"pass":[]}
#         df=pd.DataFrame(df_table)
#         user_table=pd.read_excel('users.xlsx',usecols=['mail'])
#         if mail_textbox.get() in list(user_table['mail']):
#             mail_textbox.configure(highlightbackground='red')
#         else:
#             user_table=pd.read_excel('users.xlsx',usecols=['id'])
#             id=int(list(user_table['id'])[-1])+1
#             df.loc[len(df)]=[id]+[mail_textbox.get()]+[cp.cripto(password.get())]

global user_id  
user_id=0
if os.path.exists(os.path.join(os.getcwd(), r"To_Do/data", "usersetting.cfg")):
    stg= open(os.path.join(os.getcwd(), r"To_Do/data", "usersetting.cfg"),"r",encoding="utf-8")
    line_text= stg.readlines()
    remember= line_text[0]
    remember=remember[13:]
     
    if len(remember)>0:
        user_id = int(remember)
        database=TinyDB(os.path.join(os.getcwd(), r"To_Do/data", "users.json"))
        db_query = Query()
        result = database.get(db_query.id == user_id)
        if str(result) =='None':
            a=login_panel()
            a.login_panel_elements()
        else:
            user_id =user_id 
        database.close()    
    else:
        a=login_panel()
        a.login_panel_elements()   

if user_id >0:
    page = boxes(user_id)
    page.panels()
    
 


if os.path.exists(os.path.join(os.getcwd(), r"To_Do/data", "users.json")):#'data/users.json'
    smootwin.root.mainloop()
else:
    print("Bağlantı Kurulamadı!")
    smootwin.root.destroy()