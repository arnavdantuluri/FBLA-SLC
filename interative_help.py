from tkinter import *

def run():
    root = Toplevel()
    root.geometry("350x500")
    root.title("Help/Guide On How to Use")
    root.resizable(0,0)
    r=0
    j=0
    for i in range(100):
        r = r + 1
        c=str(222222+r)
        Frame(root,width=10, height=500, bg="#"+c).place(x=j, y=0)
        j = j+10

    # Frame(root, width=250, height=400, bg="white").place(x=50, y=50)

    para = "TravelX Was developed to help people decide where they want to go, where they want to eat, or what they want to do. \n With this in mind I have developed a streamlined process to provide this functionality. \n Simply log in or sign up and proceed to the homepage where you can click on the button in the top left corner. \n Pressing this opens a hamburger menu from which you can choose what you are looking for. \n You can choose from a variety of options including restaurants, tourist attractions, and recreational activities. \n Once taken to the screen input the desired field. Slide the slider to choose a distance in miles. Click the dropdown to select a minimum rating and price(if available). \n Socket Error: There is sometimes a socket error or a JSON error that occurs due to ip bouncing or overuse of the requests library. There is no feasible solution to solving this and if this occurs simply restart the program and it will work as intended."
    text = Text(root, bg="white", width=30)
    text.insert(INSERT, para)
    text.config(state=DISABLED)
    text.place(x=50, y=60)
    root.mainloop()