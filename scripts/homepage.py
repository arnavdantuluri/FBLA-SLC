from tkinter import *
from PIL import Image, ImageTk
import food
import recreation as recreation
import tourist as tourist
from location import get_ip


#main function creates the tkinter screen

def run():
    root = Toplevel()
    root.geometry("900x500")
    root.config(bg="#262626")
    root.resizable(0,0)
    root.title("Home Page")


    #toggles the hamburger menu that allows a user to choose what they want recommended to them
    def toggle_win():
        f1 = Frame(root,width=300,height=500,bg="#12c4c0")
        f1.place(x=0,y=0)

        def bttn(x,y,text,bcolor,fcolor,cmd):
                
            def on_entera(e):
                myButton1['background'] = bcolor
                myButton1['foreground'] = "#262626"

            def on_leavea(e):
                myButton1['background'] = fcolor
                myButton1['foreground'] = "#262626"
                
            myButton1 = Button(f1, text=text, width=42,
                                height=2, fg="#262626", border=0,
                            highlightbackground=fcolor, activebackground=bcolor, activeforeground="#262626",command=cmd)

            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)

            myButton1.place(x=x, y=y)
        
        #opens the window that recommends restaurants
        def open_food():
            food.run()


        #opens the window that recommends recreational activities
        def open_recreation():
            recreation.run()


        #opens the window that recommends tourist activities
        def open_tourist():
            tourist.run()
        
        #Defines the buttons that take us to tke pages
        bttn(0,80,"R E S T A U R A N T",'#0f9d9a', '#12c4c0',open_food)
        bttn(0,154,"T O U R I S T  A T T R A C T I O N S",'#0f9d9a', '#12c4c0',open_tourist)
        bttn(0,228,"R E C R E A T I O N",'#0f9d9a', '#12c4c0',open_recreation)


        #closes the hamburger menu
        def dele():
            f1.destroy()
                    
        global img2

        img2=ImageTk.PhotoImage(Image.open("scripts/imgs/close.png"))

        Button(f1,text="close",image=img2, command=dele, borderwidth=0, activebackground="#12c4c0", bg="#12c4c0").place(x=5,y=10)


    #Welcoming user label
    l1 = Label(root, text="Welcome User",fg='white', bg='#262626')
    l1.config(font=("Comic Sans MS", 90))
    l1.place(x=50 ,y=100)


    #Displaying user location label
    ll = Label(root, text = "Location: ", bg="#262626", fg="white")
    ll.config(font=("Comic Sans MS", 20))
    ll.place(x=60, y=300)


    city, state = get_ip()
    
    loc = (str(city + ", " + state))


    e1 = Label(root, fg="white", bg="#262626", text=loc)
    e1.config(font=("Comic Sans MS", 20))
    e1.place(x=200, y=300)


    l2 = Label(root, text="Call Trafalgar For Organized Tours: +1 (866) 513-1995", fg='white', bg="#262626")
    l2.config(font=("Comic Sans MS", 20))
    l2.place(x=60, y=375)

    img1=ImageTk.PhotoImage(Image.open("scripts/imgs/open.png"))
    Button(root, image = img1,command=toggle_win, borderwidth=0, bg="#262626", activebackground="#262626", text="open").place(x=5,y=10)


    root.mainloop()
