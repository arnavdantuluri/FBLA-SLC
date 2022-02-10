import googlemaps
from location import get_ip
import time

API_KEY = "AIzaSyCURmqCLnQTMHKPO3W-2vFrrR7Mpz5DNB4"

client = googlemaps.Client(API_KEY)

def conv_miles(miles):
    try:
        return miles * 1609.344
    except:
        return 0
def get_locs(search_string, distance):

    loc = get_ip()
    geocode = client.geocode(address=loc)
    (lat, lng) = map(geocode[0]['geometry']['location'].get, ('lat', 'lng'))

    distance = conv_miles(distance)
    if search_string is None:
        search_string = "Italian"

    business_list = []

    response = client.places_nearby(
        location=(lat, lng),
        keyword=search_string,
        radius=distance
    )   

    business_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')


    while next_page_token:
        time.sleep(2)
        response = client.places_nearby(
            location=(lat, lng),
            keyword=search_string,
            radius=distance,
            page_token=next_page_token
        )   
        business_list.extend(response.get('results'))
        next_page_token = response.get('next_page_token')
    # for i in range(len(business_list)):
    #     key = "price_level"
    #     if key in business_list[i].keys():
    #         print(business_list[i]['name'])
    #         print(business_list[i]['icon'])
    #         print(business_list[i]['price_level'])
    #         print(business_list[i]['rating'])


    return business_list


# business_list = get_locs("Rock Climbing", 100)
# print("Hello!!")
# for i in range(len(business_list)):
#         key = "price_level"
#         key2 = 'rating'
#         min_rating = 3
#         max_price=3
#         if key in business_list[i].keys() and key2 in business_list[i].keys():
#             if business_list[i]['price_level'] <= min_rating and business_list[i]['rating'] >= max_price: 
#                 print(business_list[i]['name'])
#                 print(business_list[i]['icon'])
#                 print(business_list[i]['price_level'])
#                 print(business_list[i]['rating'])
#                 continue
    
# print(business_list[i])

