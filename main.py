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


def parse_one_page(driver):  # 한휘
    # 데이터 추출
    date = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/article/header/div/span[1]/a/time[1]')
    title = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/article/header/h1')
    scripture = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/article/div/p[2]')
    content = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/article/div/p[3]')
    prayer = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/main/article/div/p[4]')

    data = [element.text for element in date]+[element.text for element in title]+[element.text for element in scripture]+[element.text for element in content]+[element.text for element in prayer] # 추출한 텍스트를 배열에 저장

    # 드라이버 종료
    driver.quit()
    print("Hello world")
    print(data)
    info = [data]
    return info


def save_to_excel(info):  # 동혁
    return


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


def parse_data(starting_date, ending_date, unit):
    # startDate, endDate
    # unit: monthly, weekly, yearly

    # open Page
    print('[DBG] Opening rorkr')
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

        # info = parse_one_page()  # 2. 한휘
        # save_to_excel(info, unit)  # 3. 동혁. unit은 기본 1달치, 첫 도전은 1달치

        move_one_date(driver)
        date_cnt -= 1
        print('[DBG] date_cnt is ' + str(date_cnt))


parse_data("2024 07 19", "2024 07 20", "")
print('End Program')

##############################################


def train_data(startDate, endDate):
    # 1. directory에서 해당 날짜의 엑셀 파일 존재하는지 확인
    # 2. OpenAI에 전달할 Prompt 작성
    # 3. API 호출하여 학습
    return


def make_single_qt(filename, date):
    # 1. OpenAI API를 통해 말씀의 실재 1일치 생성
    # 2. 제목, 날짜, 내용 등을 Word 문서 형태에 맞게 저장 (filename 파일에 concat)
    return


def make_multiple_qt(cnt):
    # 1. filename 워드 파일 생성
    # 2. cnt만큼 make_single_qt 함수 호출, 날짜 전달
    # 3. filename 워드 파일 최종 저장
    return


def automate_qt():
    # 1. 다음달 날짜 계산하기
    # 2. make_multiple_qt에 날짜 전달하여 파일 만들기
    # 3. 메일로 출판사, 본인 등 관련자들에게 자동 메일 발송
    return


# git/github 기본
# pull: repository -> local
# commit: 작업한 걸 -> local (작업 단위로 commit) #comment
# # push: local -> Repository (하루 단위로 push 한다)
