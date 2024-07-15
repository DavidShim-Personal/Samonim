def parseData(startDate, endDate, unit):
    # startDate, endDate
    # unit: monthly, weekly, yearly
    # initialize(unit)
    date = startDate
    while date < endDate: # 1. 하준
        info = parse_one_page() # 2. 한휘
        save_to_excel(info, unit) # 3. 동혁. unit은 기본 1달치, 첫 도전은 1달치

        move_one_date()
        date += 1
    return


def parse_one_page(): # 한휘
    info = []
    return info


def save_to_excel(info): # 동혁

    return


def move_one_date():
    # 1. 뒤로 가기
    # 2. 다음 날짜 찾기
    # 2-1. 다음이 10 이하면 article 누러주기
    # 2-2. 10초과면: 다음페이지 넘어가기 버튼 누르고, 혀냊 page는 1번으로 초기화
    return


##############################################
def train_data(startDate, endDate):
    # directory에서 해당 날짜의 엑셀 파일 존재하는지 확인
    # OpenAI API를 통해서 학습
    return


def test_data(cnt):
    # cnt만큼 샘플 생성
    # OpenAI API를 통해서 chatbot한테 말 걸기
    # cnt횟수만큼 반복
    # word 파일에 
    return


def make_monthly_qt(date_cnt):
    # OpenAI api로 하나씩 받아오는 함수
    # n회 반복해서 word에 저장
    # 위 함수와 동작은 동일하고, 자동화를 추가한다 (특정 날짜에 시작 + 메일로 보내기)
    return

# pull: repository -> local
# commit: 작업한 걸 -> local (작업 단위로 commit) #comment
# # push: local -> Repository (하루 단위로 push 한다)
