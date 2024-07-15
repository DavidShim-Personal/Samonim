def parseData(startDate, endDate, unit):
    # startDate, endDate
    # unit: monthly, weekly, yearly
    # initialize(unit)
    date = startDate
    while date < endDate:  # 1. 하준
        info = parse_one_page()  # 2. 한휘
        save_to_excel(info, unit)  # 3. 동혁. unit은 기본 1달치, 첫 도전은 1달치

        move_one_date()
        date += 1
    return

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 웹드라이버 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 창을 열지 않고 실행하기 위한 옵션
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 웹드라이버 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 웹사이트 열기
url = 'http://rorkr.com/%eb%8b%b9%ec%8b%a0%ec%9d%98-%ed%97%8c%ea%b8%88%ec%9d%84-%ea%b3%84%ed%9a%8d%ed%95%98%ec%8b%ad%ec%8b%9c%ec%98%a4/'  # 데이터를 추출할 웹사이트의 URL
driver.get(url)



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


def move_one_date():
    # 1. 뒤로 가기
    # 2. 다음 날짜 찾기
    # 2-1. 다음이 10 이하면 article 누러주기
    # 2-2. 10초과면: 다음페이지 넘어가기 버튼 누르고, 혀냊 page는 1번으로 초기화
    return


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