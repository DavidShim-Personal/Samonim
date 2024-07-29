from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
import time

import pandas as pd
import os

def initialize_driver():
    # 크롬 웹드라이버 설정
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 브라우저 창을 열지 않고 실행하기 위한 옵션
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 웹드라이버 실행
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def parse_one_page(driver): # 한휘
    # 데이터 추출
    date = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/main/article/header/div/span[1]/a/time[1]')
    title = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/main/article/header/h1')
    scripture = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/main/article/div/p[2]')
    content = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/main/article/div/p[3]')
    prayer = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/main/article/div/p[4]')

    data = [date.text, title.text, scripture.text, content.text, prayer.text]
    
    # 데이터 출력
    print("Extracted data:", data)
    return data

def move_one_date(driver):
    next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/main/nav/div/div/a')
    next_button.click()

def days_between_dates(start_date_str, end_date_str):
    print('[DBG] Start date is ' + start_date_str)
    print('[DBG] End date is ' + end_date_str)
    date_format = "%Y %m %d"

    try:
        start_date = datetime.strptime(start_date_str, date_format)
        end_date = datetime.strptime(end_date_str, date_format)

        # 두 날짜 간의 차이 계산
        delta = end_date - start_date

        # delta.days를 통해 일 수를 구할 수 있음
        return delta.days + 1

    except ValueError:
        return "올바른 날짜 형식이 아닙니다."

def save_to_excel(array_of_strings, file_name):
    """
    주어진 문자열 배열을 엑셀 파일에 저장합니다.
    기존 파일이 존재하면 데이터를 추가하고, 존재하지 않으면 새로운 파일을 생성합니다.
    
    Parameters:
    array_of_strings (list): 저장할 문자열 배열
    file_name (str): 저장할 엑셀 파일 이름
    """
    # 새로운 데이터 프레임 생성
    new_df = pd.DataFrame([array_of_strings])
    
    if os.path.exists(file_name):
        # 기존 파일이 존재하면 파일을 읽어옵니다.
        existing_df = pd.read_excel(file_name, header=None)
        # 기존 데이터에 새로운 데이터를 추가합니다.
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    else:
        # 파일이 존재하지 않으면 새로운 데이터 프레임을 사용합니다.
        updated_df = new_df

    #파일에 데이터 저장 (처음에 한번은 파일을 만들어주고, 이후 부터는 이 df 변수를 갖고 있어서 매번 concat만)
    updated_df.to_excel(file_name, index=False, header=False)

def parse_data(starting_date, ending_date, unit):
    # startDate, endDate
    # unit: monthly, weekly, yearly

    # open Page
    driver = initialize_driver()
    url = 'http://rorkr.com/'  # 데이터를 추출할 웹사이트의 URL
    driver.get(url)

    FIRST_PAGE_TAG = '/html/body/div[1]/div/div/div/div/main/article[1]/header/h3/a'

    # Wait for page to open
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, FIRST_PAGE_TAG))
    )

    # open first page
    first_page_btn = driver.find_element(By.XPATH, FIRST_PAGE_TAG)
    first_page_btn.click()

    date_cnt = days_between_dates(starting_date, ending_date)
    print('[DBG] date_cnt is ' + str(date_cnt))
    
    # repeat for several pages
    while date_cnt > 0:
        time.sleep(3)  # [TODO] Delete after debugging is done

        info = parse_one_page(driver)
        save_to_excel(info, 'output.xlsx')

        move_one_date(driver)
        date_cnt -= 1
        print('[DBG] date_cnt is ' + str(date_cnt))

    driver.quit()

parse_data("2024 06 19", "2024 07 20", "")
print('End Program')
