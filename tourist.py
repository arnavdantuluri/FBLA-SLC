from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from location import get_ip
import tkinter as tk
from tkinter import messagebox
from mapsApi import get_locs, conv_miles
import googlemaps
import folium


#price callback to return the price inputted by user
def price_callback(selection):
    global price 
    price = selection


#distance callback to return the distance inputted by user
def distance_callback(selection):
    global distance
    distance = selection


#tourism callback to return the type of tourist activity chosen by the user
def tourist_callback(selection):
    global attraction
    attraction = selection


#rating callback to return the minimum rating inputted by user 
def rating_callback(selection):
    global user_rating
    user_rating = selection


#main function creates the tkinter screen
def run():
    
    root = Tk()
    root.geometry('500x500')
    root.resizable(0,0)
    root.config(bg="#262626")
    root.title("Tourist")

    images = [] #place read image in array to prevent python garbage collector deleting memory

    variable = StringVar(root)
    variable.set("Historical Attractions") # default value

    variable_rating = StringVar(root)
    variable_rating.set("1") #default values
    global entered_rating_by_user


    #Attraction Label
    attraction_label = Label(root, text="Attraction Type: ", fg="white", bg="#262626")
    attraction_label.config(font=("Comic Sans MS", 20))
    attraction_label.place(x=20, y=100)

    #Attraction Dropdown
    attraction_dropdown_menu = OptionMenu(root, variable,'Historical Attractions', "Monuments", "Museum", "Education", command=tourist_callback)
    attraction_dropdown_menu.config(bg="#262626", fg="white", highlightthickness=0, width=20, height=2)
    attraction_dropdown_menu.place(x=250, y=100)

    #Distance Label
    distance_label = Label(root, text="Distance: ", fg='white', bg="#262626")
    distance_label.config(font=("Comic Sans MS", 20))
    distance_label.place(x=150, y=160)


    #Distance slider
    distance_slider = Scale(root, from_=10, to=200, length=500, orient=HORIZONTAL, command=distance_callback)
    distance_slider.config(bg="#262626", fg="white")
    distance_slider.place(x=0, y=200)


    #Use Pillow to load images
    global img1
    img1 = Image.open("addButton.png")
    img2 = ImageTk.PhotoImage(img1)

    images.append(img2)

    #Location label         
    location_label = Label(root, text = "Location: ", bg="#262626", fg="white")
    location_label.config(font=("Comic Sans MS", 20))
    location_label.place(x=20, y=50)

    #rating
    rating_label = Label(root, text="Minimum Rating: ", bg="#262626", fg='white')
    rating_label.config(font=("Comic Sans MS", 20))
    rating_label.place(x=20, y=275)

    #rating entry
    rating_dropdown = OptionMenu(root, variable_rating,  '1', '2', '3', '4',  command=rating_callback)
    rating_dropdown.config(bg="#262626", fg="white", highlightthickness=0, width=10, height=2)
    rating_dropdown.place(x=250, y=275)


    
    #Get ip adress of user
    global loc
    city, state = get_ip()
    loc = (str(city + ", " + state))

    #Provides entry for user to enter location if location is incorrect
    location_entry = Label(root, fg="white", bg="#262626", text=loc)
    location_entry.config(font=("Comic Sans MS", 20))
    location_entry.place(x=150, y=50)


    def check_entries():
        get_locations_and_check()


    image = Image.open("add_button.png")
    image = ImageTk.PhotoImage(image)

    #Generate places Button
    gen_btn = Button(root, height=5, width=20, borderwidth=0, border=0, text="Find Match", bg="#12c4c0", fg="white", command=check_entries)
    gen_btn.config(font=("Comic Sans MS", 10))
    gen_btn.place(x=150, y=350)

    
    root.mainloop()


def index_in_list(a_list, index):
    print(index < len(a_list))



'''
Gets the business that match the user request using a function called get_locs() which is defined in the mapsApi
Filters the locations based on the minimum rating provided by the user and the maximum price provided by the user
'''

def get_locations_and_check():
    

    filtered_business_list = []
    business_list = []

    try:
        search_string = str(attraction)
        entered_distance = int(distance)
        entered_rating = int(user_rating)
        business_list = get_locs(search_string, entered_distance)
    except:
        messagebox.showinfo("ERROR", "PLEASE INPUT VALUES/SLIDE SLIDER")
    i = 0
    if len(business_list) > 3:
        while(len(filtered_business_list) < 3):
            key = "price_level"
            key2 = "rating"
            # print(business_list[i])
            if key2 in business_list[i].keys():
                rating_level = (business_list[i]['rating'])
                if (entered_rating) >= int(rating_level):
                    filtered_business_list.append(business_list[i])
            i+=1
    else:
        messagebox.showinfo("ERROR","PLEASE INCREASE DISTANCE")

    global names, business_rating, business_location
    names = []
    business_rating = []
    business_location = []
    
    if len(filtered_business_list) > 0:
        for i in range(len(filtered_business_list)):
            names.append(filtered_business_list[i]['name'])
            business_rating.append(filtered_business_list[i]['rating'])
            business_location.append(filtered_business_list[i]['vicinity'])
            display_reccomendations()

def display_reccomendations():
    root = Toplevel()
    root.geometry("700x700")
    root.title("Login")
    root.resizable(0,0)
    root.config(bg="#262626")
    display_map()

    try:
        business_name_label = Label(root, text=names[0], bg="#262626", fg='white')
        business_name_label.config(font=("Comic Sans MS", 20))
        business_name_label.place(x=25, y=50)

        business_location_label = Label(root, text="Location: " + str(business_location[0]), bg="#262626", fg='white')
        business_location_label.config(font=("Comic Sans MS", 20))
        business_location_label.place(x=25, y=150)

        business_rating_label = Label(root, text="Rating: " + str(business_rating[0]), bg="#262626", fg='white')
        business_rating_label.config(font=("Comic Sans MS", 20))
        business_rating_label.place(x=25, y=250)
    except:
        pass

    root.mainloop()


def display_map():

    API_KEY = "AIzaSyCURmqCLnQTMHKPO3W-2vFrrR7Mpz5DNB4"

    client = googlemaps.Client(API_KEY)

    geocode = client.geocode(loc)

    lat = geocode[0]['geometry']['location']['lat']
    longi = geocode[0]['geometry']['location']['lng']
    print(lat)
    print(longi)
    m = folium.Map(location=[lat,longi], zoom_start=15)
    

    location = business_location[0]
    city = loc



    geocode_result = client.geocode(str(location) +' '+ city)
    if len(geocode_result) > 0:
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude =  geocode_result[0]['geometry']['location']['lng']
    print(latitude)
    print(longitude)
    folium.Marker([lat, longi], popup="<h1> Location </h1>").add_to(m)
    folium.Marker([latitude, longitude], popup="<h1> Restaurant </h1>").add_to(m)
    m.save('tourist_map.html')