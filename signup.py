from tkinter import *
from tkinter import messagebox
from turtle import home
import homepage
from PIL import Image, ImageTk
import interative_help 
import sqlite3




def toggle_password():
    if password_entry.cget("show") == '':
        password_entry.config(show = '*')
    else:
        password_entry.config(show='')


def run():
    w=Toplevel()
    w.geometry("350x500")
    w.title("Signup")
    w.resizable(0,0)
    r=0
    j=0
    for i in range(100):
        r = r + 1
        c=str(124529+r)
        Frame(w,width=10, height=500, bg="#"+c).place(x=j, y=0)
        j = j+10

    Frame(w, width=250, height=400, bg="white").place(x=50, y=50)
    Frame(w,width=180,height=2,bg="#141414").place(x=80,y=250)
    Frame(w,width=180,height=2,bg="#141414").place(x=80,y=330)


    login_image = Image.open("log.png")
    login_image_modified = ImageTk.PhotoImage(login_image)

    label1=Label(w, image=login_image_modified, border=0,justify=CENTER).place(x=115, y=50)

    password_show = Image.open("2072008.jpg")
    password_show = password_show.resize((50, 40))
    password_show_modified = ImageTk.PhotoImage(password_show)

    username_label=Label(w, text="Username: ", bg='white')

    username_label.config(font=1)
    username_label.place(x=80, y=200)

    username_entry = Entry(w, width=20, border=0)
    username_entry.config(font=1)
    username_entry.place(x=80,y=230)

    password_label=Label(w, text="Password: ", bg='white')

    password_label.config(font=2)
    password_label.place(x=80, y=280)


    pass_show_bool = False
    global password_entry
    password_entry = Entry(w, width=20, border=0, show="*")
    password_entry.config(font=1)
    password_entry.place(x=80,y=310)
    show_password = Button(w, width=35,  image=password_show_modified, command=toggle_password, borderwidth=0, bg="white").place(x=235,y=290)

    def create_user():
        database = sqlite3.connect("login.sqlite")
        cursor = database.cursor()
        cursor.execute("SELECT username FROM login where username='%s'" % username_entry.get())
        row = cursor.fetchone()
        if row:
            messagebox.showinfo("SIGNUP UNSUCCESSFUL", "      USER ALREADY EXISTS PLEASE LOGIN         ")
        else:
            database.execute("INSERT INTO login(username, password) VALUES (?, ?)", (str(username_entry.get()), str(password_entry.get())))
            messagebox.showinfo("SIGNUP SUCCESSFUL", "      PLEASE LOGIN         ")
            print("Added User")

        cursor.connection.commit()
        database.close()
        w.quit()


    signup_button = Button(w,width=15,height=2,bg="#994422",border=0,command=create_user, text="Signup").place(x=120,y=400)

    w.mainloop()