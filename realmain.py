from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
import time 

def initialize_driver():
    # 크롬 웹드라이버 설정
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 브라우저 창을 열지 않고 실행하기 위한 옵션
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 웹드라이버 실행
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver = initialize_driver()
url = 'http://rorkr.com/'  # 데이터를 추출할 웹사이트의 URL
driver.get(url)

try:
    # WebDriverWait를 사용하여 요소가 나타날 때까지 기다립니다 (예: 10초)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div/main/nav/div/div[1]'))
    )

except Exception as e:
    print(e)  # 오류 메시지 출력

finally:
    driver.quit()

def days_between_dates(start_date_str, end_date_str):
    date_format = "%Y %m %d"

    try:
        start_date = datetime.strptime(start_date_str, date_format)
        end_date = datetime.strptime(end_date_str, date_format)
        
        # 두 날짜 간의 차이 계산
        delta = end_date - start_date
        
        # delta.days를 통해 일 수를 구할 수 있음
        return delta.days
    
    except ValueError:
        return "올바른 날짜 형식이 아닙니다."

def move_one_date():
    # 1. 뒤로 가기
    # 2. 다음 날짜 찾기
    # 2-1. 다음이 10 이하면 article 눌러주기
    # 2-2. 10초과면: 다음페이지 넘어가기 버튼 누르고, 현재 page는 1번으로 초기화
    site=driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/main/nav/div/div[1]')
    site.click()

def parse_data(starting_date, ending_date, ): # +unit
    # startDate, endDate
    # unit: monthly, weekly, yearly
    # initialize(unit)
    # date = startDate

    

    date1=days_between_dates(starting_date, ending_date)
    enter=driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/main/article[1]')
    enter.click()

    # while date < endDate:  # 1. 하준
    while date1 > 0:
        time.sleep(3)
        
        # info = parse_one_page()  # 2. 한휘
        # save_to_excel(info, unit)  # 3. 동혁. unit은 기본 1달치, 첫 도전은 1달치

        # move_one_date()
        date1 -= 1 
    

parse_data("2024 07 19", "2024 07 16")
move_one_date()

def parse_one_page():  # 한휘
    # 데이터 추출
    date = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/article/header/div/span[1]/a/time[1]')
    title = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/article/header/h1')
    scripture = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/article/div/p[2]')
    content = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/article/div/p[3]')
    prayer = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/article/div/p[4]')

    data = [element.text for element in date]+[element.text for element in title]+[element.text for element in scripture]+[element.text for element in content]+[element.text for element in prayer] # 추출한 텍스트를 배열에 저장

    # 드라이버 종료
    driver.quit()

    print(data)
    info = [data]
    return info


def save_to_excel(info):  # 동혁
    return