from tkinter import *
from tkinter import messagebox
from turtle import home
import homepage
from PIL import Image, ImageTk
import interative_help 
import sqlite3
import signup

w=Tk()
w.geometry("350x500")
w.title("Login")
w.resizable(0,0)

# Can be used in place of sql database
# users = {
#     "Arnav Dantuluri" : "Hello!",
#     "Ishika Dantuluri" : "Hello!",
#     "Arunima Mantena" : "Hello!",
#     "Satya Dantuluri" : "Hello!",
#     "Loki Dantuluri" : "Hello!"
# }
# isUser = False


#Shows and hides the password field
def toggle_password():
    if password_entry.cget("show") == '':
        password_entry.config(show = '*')
    else:
        password_entry.config(show='')


#Connects to the database and checks the user with the database of users available
#Checks if the user exists or not
def login():
    print("Hello!")
    database = sqlite3.connect('login.sqlite')
    database.execute('CREATE TABLE IF NOT EXISTS login(username TEXT, password TEXT)')
    cursor = database.cursor()
    cursor.execute("SELECT * FROM login where username=? AND password=?", (username_entry.get(), password_entry.get()))
    row = cursor.fetchone()
    if row:
        messagebox.showinfo("LOGIN SUCCESSFUL", "      WELCOME         ")
        w.quit()
        homepage.run()
    else:
        messagebox.showinfo("LOGIN UNSUCCESSFUL", "      PLEASE TRY AGAIN       ")
    cursor.connection.commit()
    database.close()

#Runs the signup screen
def signup_user():
    signup.run()


#script to generate gradient background
r=0
j=0
for i in range(100):
    r = r + 1
    c=str(222222+r)
    Frame(w,width=10, height=500, bg="#"+c).place(x=j, y=0)
    j = j+10

Frame(w, width=250, height=400, bg="white").place(x=50, y=50)

def help_func():
    interative_help.run()


password_show = Image.open("scripts/imgs/2072008.jpg")
password_show = password_show.resize((50, 40))
password_show_modified = ImageTk.PhotoImage(password_show)

help_image = Image.open("scripts/imgs/download.png")
help_image = help_image.resize((40, 40))
help_image_modified = ImageTk.PhotoImage(help_image)

help_button = Button(w, image=help_image_modified, borderwidth=0, bg="white", command=help_func)
help_button.place(x=235, y=340)

#label
username_label=Label(w, text="Username: ", bg='white')

username_label.config(font=1)
username_label.place(x=80, y=200)

username_entry = Entry(w, width=20, border=0)
username_entry.config(font=1)
username_entry.place(x=80,y=230)

#label2
password_label=Label(w, text="Password: ", bg='white')

password_label.config(font=2)
password_label.place(x=80, y=280)


pass_show_bool = False
password_entry = Entry(w, width=20, border=0, show="*")
password_entry.config(font=1)
password_entry.place(x=80,y=310)
show_password = Button(w, width=35,  image=password_show_modified, command=toggle_password, borderwidth=0, bg="white").place(x=235,y=290)

Frame(w,width=180,height=2,bg="#141414").place(x=80,y=250)
Frame(w,width=180,height=2,bg="#141414").place(x=80,y=330)

login_image = Image.open("scripts/imgs/log.png")
login_image_modified = ImageTk.PhotoImage(login_image)

label1=Label(image=login_image_modified, border=0,justify=CENTER)
label1.place(x=115, y=50)


# Used if dictionoary is used for user storage rather than sql database
# def cmd(isUser):
#     for user in users:
#         if usernme_entry.get() == user and password_entry.get() == users[user]:
#             isUser = True
#             username = (usernme_entry.get())
#     if isUser:
#         messagebox.showinfo("LOGIN SUCCESSFUL", "      WELCOME " + username.upper() + "        ")
#         w.quit()
#         homepage.run()
#     else:
#         messagebox.showinfo("LOGIN UNSUCCESSFUL", "      PLEASE TRY AGAIN       ")
            

login_button = Button(w,width=15,height=2,bg="#994422",border=0,command=login, text="Login").place(x=60,y=400)
signup_button = Button(w,width=15,height=2,bg="#994422",border=0,command=signup_user, text="Signup").place(x=180,y=400)

w.mainloop()
