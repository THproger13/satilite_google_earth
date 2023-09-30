import requests
from geopy.geocoders import Nominatim
import webbrowser

api_key = "AIzaSyDjb2nlzcWFbaInEqtarv2OIEyM2nZh8lM"  # API 키를 여기에 입력하세요.
geolocator = Nominatim(user_agent='South Korea', timeout=None)

user_location = "문학경기장"
location = geolocator.geocode(user_location)

latitude, longitude = location.latitude, location.longitude  # 위도와 경도를 지정합니다.

url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=500&key={api_key}"

response = requests.get(url)

if response.status_code == 200:
    places = response.json()['results']
    for place in places:
        print(f"Name: {place.get('name', 'N/A')}")
        print(f"Address: {place.get('vicinity', 'N/A')}")
        print(f"Type: {', '.join(place.get('types', ['N/A']))}")
        print("------")
else:
    print("Error:", response.status_code)
