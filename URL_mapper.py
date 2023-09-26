from geopy.geocoders import Nominatim

# 사용자 음성명령에서 추출한 지역명
user_location = "New York"

# Geopy를 사용하여 지역명을 좌표로 변환
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode(user_location)

if location:
    # 변환된 좌표 정보
    latitude = location.latitude
    longitude = location.longitude

    # 구글 어스 URL 생성 (예시)
    google_earth_url = f"https://earth.google.com/web/@{latitude},{longitude},0a,10000d,0h,0t,0r"
    
    # Selenium 또는 웹 브라우저를 사용하여 구글 어스로 이동
    # ...

else:
    print("지역을 찾을 수 없습니다.")
