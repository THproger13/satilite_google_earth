import ee
ee.Authenticate()
ee.Initialize()
print(ee.Image("NASA/NASADEM_HGT/001").get("title").getInfo())

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Chrome WebDriver 초기화
# driver = webdriver.Chrome()

# # Google Earth 웹 페이지로 이동
# driver.get('https://earth.google.com/web')

# # 검색창 요소를 찾아 입력
# search_box = driver.find_element_by_class_name('flt-text-editing')
# search_query = '서울대공원'  # 원하는 지역명을 여기에 입력
# search_box.send_keys(search_query)
# search_box.send_keys(Keys.RETURN)  # Enter 키를 눌러 검색 실행

# # 검색 결과가 로드될 때까지 대기 (예: 10초)
# wait = WebDriverWait(driver, 10)
# search_results = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'g3-tooltip-content')))

# # 원하는 작업을 수행한 후에 브라우저를 종료
# # 여기에서는 10초 대기 후에 종료하도록 예시로 작성했습니다.
# # 실제 작업에 따라 더 많은 동작을 추가하실 수 있습니다.
# time.sleep(10)

# # 브라우저 종료
# driver.quit()
