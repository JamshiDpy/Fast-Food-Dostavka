import folium
import openrouteservice
from openrouteservice import convert
import simplejson, urllib
import requests

from geopy import distance
import gmaps

# gmaps.configure(api_key="f1dd6bc8e8cae345d6d081f1b78b293899edb796")
#
# location1 = 40.626183, 72.500744
# location2 = 40.599440, 72.495961
# layer = gmaps.Directions(location1, location2, mode='driving')
#
# fig = gmaps.figure()
# fig.add_layer(layer)

# fig


#
# print(location1)
#
# print(distance.great_circle(location1, location2))


# url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={
# 1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord),str(dest_coord)) result= requests.get(
# url).json() print(result) driving_time = result['rows'][0]['elements'][0]['duration']['value'] print(
# '----------------------------------------------') print(driving_time)

# client = openrouteservice.Client(key="5b3ce3597851110001cf62486ccb0708a3b944caaf2c12168b46ed13")
#
# # coords = ((40.62621353367795, 72.5008179405125), (40.599429, 72.495991))
# coords = ((40.626183, 72.500744), (40.599440, 72.495961))
# # coords = ((80.21787585263182,6.025423265401452),(80.23990263756545,6.018498276842677))
# res = client.directions(coords)
#
# print(res)

# print(type(-12132323))
# print(-1212121)
# from data.config import ChannelInside
# print(type(ChannelInside))
# print(ChannelInside)
#
# 40,599429
# 72,495991

from geopy import Nominatim

# geolocator = Nominatim(user_agent="dostavka _bot")
#
# location = geolocator.reverse("40.599429, 72.495991")
#
# print(location.address)


# result = None
#
# a = True
# b = False
# result = b * a
#
# print(result)

import json
# a = {'id': 87, 'user': {'id': 2, 'telegram_id': 966430294, 'phone_number': '998911701312', 'telegram_username': 'birikkiuchtortbesholtiyetti', 'language': 'uz'}, 'orders': [{'id': 58, 'user': {'id': 2, 'telegram_id': 966430294, 'phone_number': '998911701312', 'telegram_username': 'birikkiuchtortbesholtiyetti', 'language': 'uz'}, 'product': {'id': 4, 'name_uz': 'Lavash kichik', 'name_ru': 'Лаваш маленький', 'category': {'id': 1, 'name_uz': 'Lavash 🌯', 'name_ru': 'Лаваш 🌯', 'child': None, 'image': '/media/category_images/Lavash_Main.jpg'}, 'description_uz': 'batafsil uz', 'description_ru': 'batafsil ru', 'image': '/media/product_images/lavash_kichik.jpg', 'price': 18000.0}, 'quantity': 4, 'total_price': "72,000 so'm", 'ordered': True}], 'latitude': '40.599429', 'longitude': '72.495991', 'date': '2024-01-26T06:58:37.230291Z'}
# # print(json.dumps(a))
# print(a['latitude'])
number = '998911701312'
import requests

url = "https://notify.eskiz.uz/api/message/sms/send"

payload = {'mobile_phone': '998911701312',
           'message': 'Eskiz Test',
           'from': '4546',
           }

headers = {
    'Authorization':
        "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDk4NzU4NDEsImlhdCI6MTcwNzI4Mzg0MSwicm9sZSI6InRlc3QiLCJzaWduIjoiZjFjNTg3OGNjM2IwM2U0OGYzMzIwOWY4NjNkMjUyZDk1ODk5NmY2M2QzZjBiNGI2MDc1MDU2NWNmOWYxMTY1ZSIsInN1YiI6IjYzNjMifQ.o2nWwxFwluhKhw-OjHtzFK1xpHGX0G0vVWDlsPtAH1c"
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
