# FBLA-SLC
Utilized Tkinter and python to develop a graphical user interface that recommends restaurants, tourist attractions, and monuments. Works by asking for a username and password which if they match the username and password given in the database leads to a menu window where you can choose what you want recommended to you using the hamburger menu. Utilizes an ip grabber using a python library called requests which calls a request on a url which returns the ip address of the user which is then converted to a geographic location using a library called geoip2 making it extremely simple for a user to search for a business or service that they desire or are looking for. Also utilizes the google maps api to search for nearby businesses and services using a search word and a distance or a radius of travel that we look for a business in. Program also contains a help button/guide to access simply click the question button on the login page

Pros: The google maps api has over 10 million places and is constantly being updated which provides a huge advantage over the 1000 or so you can manually input into a database. The sqlite database is extremely lightweight and does not require a server to run

Cons: The google maps api costs money but google does provide $200 worth of free credit. Because sqlite is so lightweight it often shuts down connections due to an overload of requests for the database. In a commercial application the sqlite database would be replaced with a mySql database or another more professional database system

Plans for improvement: Plan on implementing a recommendation system which will utilize the database of users and also implement a link to a website which contains a forum for users to ask questions and to interact with other users (will be built using django). I also plan on making the output menu more interactive.

Requirements:

Python 3.7 or greater preferably 3.10

Windows operating system formatting doesn't work on MacOS

google maps library (pip install googlemaps)

geoip2 library (pip install geoip2)

requests library (pip install requests)

pillow library (pip install Pillow)

folium library (pip install folium)


# Note:
If the return page return a 0 as a rating it is because the rating does not exist and it is the only service under those certain parameters which is why it is returned
