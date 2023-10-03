import requests
from geopy.geocoders import Nominatim
import time

api_key = "AIzaSyDjb2nlzcWFbaInEqtarv2OIEyM2nZh8lM"  # 실제 API 키를 여기에 입력하세요.
geolocator = Nominatim(user_agent='South Korea', timeout=None)

user_location = "구월동 로데오거리"
location = geolocator.geocode(user_location)

latitude, longitude = location.latitude, location.longitude  # 위도와 경도를 지정합니다.
radius = "100"  # 반경을 지정합니다.

url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius}&key={api_key}"

def fetch_places(url):
    all_places = []
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            all_places.extend(result.get('results', []))
            
            # next_page_token이 있으면 다음 페이지의 결과를 가져옵니다.
            next_page_token = result.get('next_page_token')
            if next_page_token:
                url = f"{url}&pagetoken={next_page_token}"
                time.sleep(2)  # API의 제한으로 인해 다음 페이지 요청 전에 약간의 대기 시간이 필요합니다.
            else:
                url = None
        else:
            print("Error:", response.status_code)
            url = None
    return all_places

all_places = fetch_places(url)
for place in all_places:
    print(f"Name: {place.get('name', 'N/A')}")
    print(f"Address: {place.get('vicinity', 'N/A')}")
    print(f"Type: {', '.join(place.get('types', ['N/A']))}")
    print("------")
