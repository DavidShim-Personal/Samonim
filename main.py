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


def parse_one_page():  # 한휘
    info = []
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
