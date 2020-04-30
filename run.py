from selenium import webdriver
import time
import sys
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument('lang=ko_KR')
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
driver = webdriver.Chrome('C:/Python/chromedriver.exe', chrome_options = options)
user_id = input("DCINSIDE 아이디를 입력해주세요..: ")
user_pw = input("DCINSIDE 비밀번호를 입력해주세요..: ")
gallog = 'https://gallog.dcinside.com/'+ user_id +'/posting/'
comment = 'https://gallog.dcinside.com/'+ user_id +'/comment/'
driver.get("https://dcinside.com")
driver.find_element_by_xpath('//*[@id="user_id"]').send_keys(user_id)
driver.find_element_by_xpath('//*[@id="pw"]').send_keys(user_pw)
driver.find_element_by_xpath('//*[@id="login_ok"]').click()
time.sleep(1)
driver.get(gallog)
gallcheck = int(input('삭제할 갤러리? (전체 갤러리는 0, 특정 갤러리는 1선택) : '))
if gallcheck == 0:
    all = int(input("지울 게시글 수(최신순, 다 지울거면 자신의 게시글수 적으세요.) : "))
    for i in range (1, all + 1):
        driver.find_element_by_xpath('/html/body/div/div[2]/main/article/div/section/div[1]/div/ul/li[1]/div[2]/div/button').click()
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(2)
        driver.refresh()
        driver.implicitly_wait(5)
        time.sleep(1)
    print("게시글 %d 개 삭제 완료!" % all)

if gallcheck == 1:
    minormajor = int(input('마이너 갤러리 경우 0, 메이저 갤러리 경우 1 입력..: '))
    if minormajor == 0:
        minor = input('갤러리 번호 입력 : ')
        migall = 'https://gallog.dcinside.com/'+ user_id +'/posting/minor?gno=' + minor
        driver.get(migall)
        driver.implicitly_wait(4)
        if driver.current_url == gallog:
            print("올바르지 않은 갤러리 번호를 입력했습니다. 5초뒤 프로그램이 자동종료됩니다.")
            time.sleep(5)
            sys.exit()
        else:
            jcount  = int(input('지울 글 개수 : '))
            for i in range (1, jcount+1):
                driver.find_element_by_xpath('/html/body/div/div[2]/main/article/div/section/div[1]/div/ul/li[1]/div[2]/div/button').click()
                alert = driver.switch_to_alert()
                alert.accept()
                time.sleep(2)
                driver.refresh()
                driver.implicitly_wait(5)
                time.sleep(1)
            print("게시글 %d 개 삭제 완료!" % jcount)
      
    if minormajor == 1:
        major = input('갤러리 번호 입력 : ')
        magall = 'https://gallog.dcinside.com/'+ user_id +'/posting/main?gno=' + major
        driver.get(magall)
        driver.implicitly_wait(4)
        if driver.current_url == gallog:
            print("올바르지 않은 갤러리 번호를 입력했습니다. 5초뒤 프로그램이 자동종료됩니다.")
            time.sleep(5)
            sys.exit()
        kcount  = int(input('지울 글 개수 : '))
        for i in range (1, kcount+1):
            driver.find_element_by_xpath('/html/body/div/div[2]/main/article/div/section/div[1]/div/ul/li[1]/div[2]/div/button').click()
            alert = driver.switch_to_alert()
            alert.accept()
            time.sleep(2)
            driver.refresh()
            driver.implicitly_wait(5)
            time.sleep(1)
        print("게시글 %d 개 삭제 완료!" % kcount)



    else:
        print("잘못 입력하셨습니다. 프로그램을 5초뒤에 종료합니다..")
        time.sleep(5)
        sys.exit()
