# FBLA-SLC
Utilized Tkinter and python to develop a graphical user interface that recommends restaurants, tourist attractions, and monuments. Works by asking for a username and password which if they match the username and password given in the database leads to a menu window where you can choose what you want recommended to you using the hamburger menu. Utilizes an ip grabber using a python library called requests which calls a request on a url which returns the ip address of the user which is then converted to a geographic location using a library called geoip2 making it extremely simple for a user to search for a business or service that they desire or are looking for. Also utilizes the google maps api to search for nearby businesses and services using a search word and a distance or a radius of travel that we look for a business in.

Pros: The google maps api has over 10 million places and is constantly being updated which provides a huge advantage over the 1000 or so you can manually input into a database. The sqlite database is extremely lightweight and does not require a server to run

Cons: The google maps api costs money but google does provide $200 worth of free credit however charges do rack up after a while. Because sqlite is so lightweight it often shuts down connections due to an overload of requests for the database. In a commercial application the sqlite database would be replaced with a mySql database

Plans for improvement: Plan on implementing a recommendation system which will utilize the database of users and also implement a link to the website of the service the google maps api returns

Requirements:

Python 3.7 or greater preferably 3.10

Windows operating system formatting doesn't work on MacOS

google maps library (pip install googlemaps)

geoip2 library (pip install geoip2)

requests library (pip install requests)

pillow library (pip install Pillow)

Note:

If you get a json or html related error close the tab and rerun it. The error is caused by socket overuse and there is no certified way to solve this
