import time
import sys
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
num = "1915053"  #学籍番号
pw = ""   #パスワード
subjects = ["資格","ラズパイ","プロジェクト"] # 勉強した科目
result = ["4","3"]  # 評価を◎か○から選択
item = ["0","0.5","1"]
tim = [" 100分"," 120分","150分","300分","240分"]

yy_mm_dd = input()
if len(yy_mm_dd) != 8:
    print ("input error")
    sys.exit()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3) # 要素が見つかるまで3秒待つ設定
#------学生ポータル-------------------------------
driver.get("https://navi.mars.kanazawa-it.ac.jp/portal/student/")
driver.find_element_by_name("uid").send_keys(num)# 学籍番号入力
driver.find_element_by_name("pw").send_keys(pw) # PW入力
time.sleep(1.5)
driver.find_element_by_id("StudentLoginBtn").click() #ログインボタンクリック
driver.find_element_by_class_name("crrclmFlow").click() #KITナビのクリック
test = driver.find_element_by_class_name("weekPortfolioBtn") #一週間の行動履歴のボタンをクリック
test.click()
#------一週間の行動履歴-------------------------------
time.sleep(1)
driver.switch_to.window(driver.window_handles[-1])
driver.switch_to.window(driver.window_handles[-1])
test = driver.find_element_by_xpath("//*[@id='Calendar']/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[2]/table/tbody/tr[1]/td[1]/a/div") #特定の週をクリック（実験用に今は複数取得）
time.sleep(2)
#----行動履歴の中身--------------------------------------
time.sleep(3)
import datetime
#start_day = datetime.date(year,month,day)
st1 = "資格の勉強を進める"
st2 = "予習、授業、復習のサイクルを維持する"
st3 = "成果物を出す"
driver.find_element_by_name("PRIORITY1").send_keys(st1)
a = random.choice("4")
Select(driver.find_element_by_name("ACHIEVEMENT1")).select_by_value(a)
driver.find_element_by_name("PRIORITY2").send_keys(st2)
b = random.choice(result)
Select(driver.find_element_by_name("ACHIEVEMENT2")).select_by_value(b)
driver.find_element_by_name("PRIORITY3").send_keys(st3)
c = random.choice(result)
Select(driver.find_element_by_name("ACHIEVEMENT3")).select_by_value(c)
#yy_mm_dd = str(input())
year = int(yy_mm_dd[0:4])
month = int(yy_mm_dd[4:6])
day = int(yy_mm_dd[6:8])

#study_item = ["数理工","線形代数","英語","イギリス","コンピューターシステム","PD","離散数学"]

#temp = driver.find_element_by_class_name("div.PageTitle")
#一週間の行動履歴（2019/12/8～2019/12/14）
#new_temp = temp.strip("一週間の行動履歴（").replace("～","/")
#year = int(new_temp.split("/")[0])
#month = int(new_temp.split("/")[1])
    #day = int(new_temp.split("/")[2])
start_day = datetime.date(year,month,day)
str_start_day = str(start_day).replace("-","/")
Sun = random.choice(subjects)
Sun1 = random.choice(item)
Sun2 = random.choice(tim)
driver.find_element_by_name("HOMEWORK_TIME."+str_start_day).send_keys(Sun + Sun2)
driver.find_element_by_name("BREAKFAST." +str_start_day ).click()
driver.find_element_by_name("LUNCH." +str_start_day ).click()
driver.find_element_by_name("DINNER." +str_start_day ).click()
Select(driver.find_element_by_name("SLEEP_TIME." + str_start_day)).select_by_value("7")
Select(driver.find_element_by_name("EXERCISE_TIME." + str_start_day)).select_by_value(Sun1)
#-------------------------
start_day = start_day + datetime.timedelta(days = 1)
str_start_day = str(start_day).replace("-","/")
Mon= random.choice(subjects)
Mon1 = random.choice(item)
Mon2 = random.choice(tim)
driver.find_element_by_name("HOMEWORK_TIME."+str_start_day).send_keys(Mon + Mon2)
driver.find_element_by_name("ACTIVITY_CONTENT."+str_start_day).send_keys
driver.find_element_by_name("BREAKFAST." +str_start_day ).click()
driver.find_element_by_name("LUNCH." +str_start_day ).click()
driver.find_element_by_name("DINNER." +str_start_day ).click()
Select(driver.find_element_by_name("SLEEP_TIME." + str_start_day)).select_by_value("7")
Select(driver.find_element_by_name("EXERCISE_TIME." + str_start_day)).select_by_value(Mon1)
#-------------------------
start_day = start_day + datetime.timedelta(days = 1)
str_start_day = str(start_day).replace("-","/")
Tue = random.choice(subjects)
Tue1 = random.choice(item)
Tue2 = random.choice(tim)
driver.find_element_by_name("HOMEWORK_TIME."+str_start_day).send_keys(Tue + Tue2)
driver.find_element_by_name("ACTIVITY_CONTENT."+str_start_day).send_keys()
driver.find_element_by_name("BREAKFAST." +str_start_day ).click()
driver.find_element_by_name("LUNCH." +str_start_day ).click()
driver.find_element_by_name("DINNER." +str_start_day ).click()
Select(driver.find_element_by_name("SLEEP_TIME." + str_start_day)).select_by_value("7")
Select(driver.find_element_by_name("EXERCISE_TIME." + str_start_day)).select_by_value(Tue1)
#-------------------------
start_day = start_day + datetime.timedelta(days = 1)
str_start_day = str(start_day).replace("-","/")
Wed = random.choice(subjects)
Wed1 = random.choice(item)
Wed2 = random.choice(tim)
driver.find_element_by_name("HOMEWORK_TIME."+str_start_day).send_keys(Wed + Wed2)
driver.find_element_by_name("BREAKFAST." +str_start_day ).click()
driver.find_element_by_name("LUNCH." +str_start_day ).click()
driver.find_element_by_name("DINNER." +str_start_day ).click()
Select(driver.find_element_by_name("SLEEP_TIME." + str_start_day)).select_by_value("7")
Select(driver.find_element_by_name("EXERCISE_TIME." + str_start_day)).select_by_value(Wed1)
#-------------------------
start_day = start_day + datetime.timedelta(days = 1)
str_start_day = str(start_day).replace("-","/")
Thu = random.choice(subjects)
Tue1 = random.choice(item)
Tue2 = random.choice(tim)
driver.find_element_by_name("HOMEWORK_TIME."+str_start_day).send_keys(Thu + Tue2)
driver.find_element_by_name("BREAKFAST." +str_start_day ).click()
driver.find_element_by_name("LUNCH." +str_start_day ).click()
driver.find_element_by_name("DINNER." +str_start_day ).click()
Select(driver.find_element_by_name("SLEEP_TIME." + str_start_day)).select_by_value("7")
Select(driver.find_element_by_name("EXERCISE_TIME." + str_start_day)).select_by_value(Tue1)
#-------------------------
start_day = start_day + datetime.timedelta(days = 1)
str_start_day = str(start_day).replace("-","/")
Fri = random.choice(subjects)
Fri1 = random.choice(item)
Fri2 = random.choice(tim)
driver.find_element_by_name("HOMEWORK_TIME."+str_start_day).send_keys(Fri + Fri2)
driver.find_element_by_name("BREAKFAST." +str_start_day ).click()
driver.find_element_by_name("LUNCH." +str_start_day ).click()
driver.find_element_by_name("DINNER." +str_start_day ).click()
Select(driver.find_element_by_name("SLEEP_TIME." + str_start_day)).select_by_value("7")
Select(driver.find_element_by_name("EXERCISE_TIME." + str_start_day)).select_by_value(Fri1)
#-------------------------
start_day = start_day + datetime.timedelta(days = 1)
str_start_day = str(start_day).replace("-","/")
Sat = random.choice(subjects)
Sat1 = random.choice(item)
Sat2 = random.choice(tim)
driver.find_element_by_name("HOMEWORK_TIME."+str_start_day).send_keys(Sat + Sat2)
driver.find_element_by_name("BREAKFAST." +str_start_day ).click()
driver.find_element_by_name("LUNCH." +str_start_day ).click()
driver.find_element_by_name("DINNER." +str_start_day ).click()
Select(driver.find_element_by_name("SLEEP_TIME." + str_start_day)).select_by_value("7")
Select(driver.find_element_by_name("EXERCISE_TIME." + str_start_day)).select_by_value(Sat1)
time.sleep(30)
#-------------------------
