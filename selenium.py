from selenium import webdriver

# 웹 드라이버 생성
driver = webdriver.Chrome()

# 웹 페이지 접속
driver.get("https://www.google.com")

# 검색어 입력
search_box = driver.find_element_by_name("q")
search_box.send_keys("검색어")

# 검색 버튼 클릭
search_box.submit()

# 검색 결과 출력
results = driver.find_elements_by_css_selector("div.g")
for result in results:
    title = result.find_element_by_css_selector("h3").text
    url = result.find_element_by_css_selector("a").get_attribute("href")
    print(title, url)

# 웹 드라이버 종료
driver.quit()# -
