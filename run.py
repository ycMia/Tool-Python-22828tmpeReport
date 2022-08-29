import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

val_StudentNum = "yourID"
val_passWord = "yourPassword"

val_month_start = 8
val_day_start = 18

val_month_end = 8
val_day_end = 29

val_month_iter = val_month_start
val_day_iter = val_day_start

def signDay(val_month,val_day) :
    driver.get("https://selfreport.shu.edu.cn/Dayreport.aspx?day=2022-"+str(val_month)+"-"+str(val_day))
    driver.implicitly_wait(5)
    clickBox_promise = driver.find_element(by=By.ID, value="p1_ChengNuo-inputEl-icon")
    clickBox_promise.click()
    driver.implicitly_wait(0.5)
    
    #在上海(不进学校)
    clickCircle_location = driver.find_element(by=By.ID, value="fineui_8-inputEl-icon")
    clickCircle_location.click()
    driver.implicitly_wait(0.5)
    
    #家庭地址
    clickCircle_isHomeLocation = driver.find_element(by=By.ID, value="fineui_24-inputEl-icon")
    clickCircle_isHomeLocation.click()
    driver.implicitly_wait(0.5)
    
    #无高风险旅居史(废话)
    clickCircle_notInRiskyArea = driver.find_element(by=By.ID, value="fineui_26-inputEl-icon")
    clickCircle_notInRiskyArea.click()
    driver.implicitly_wait(0.5)
    
    #未被判定为密接(还是废话)
    clickCircle_isNotIDIOT = driver.find_element(by=By.ID, value="fineui_31-inputEl-icon")
    clickCircle_isNotIDIOT.click()
    driver.implicitly_wait(0.5)
    
    #提交
    submit_button_DayReportPage = driver.find_element(by=By.ID, value = "p1_ctl01_btnSubmit")
    submit_button_DayReportPage.click()
    driver.implicitly_wait(0.5)
    
    #你妈的确定
    comfirm_button_DayReportPage_afterBox = driver.find_element(by=By.ID,value = "fineui_39")
    comfirm_button_DayReportPage_afterBox.click()
    driver.implicitly_wait(2)
    
    print("================DayCompleted: "+str(val_month)+"-"+str(val_day))
    input()
    return
    pass

#didn't done bissextile year adjust
def doMonthAddAdjust(val_month,val_day):
    if(val_day == 29 and val_month == 2):
        return True
    elif(val_day >= 31):
        if(val_day == 32 and val_month == 1 or val_month == 3 or val_month == 5 or val_month == 7 or val_month == 8 or val_month == 10 or val_month == 12):
            return True
        elif(val_day == 31 and val_month == 4 or val_month == 6 or val_month == 9 or val_month == 11):
            return True
        else:
            return False
    else:
        return False
    pass

driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://selfreport.shu.edu.cn/")

driver.implicitly_wait(5)

print("================start")
username_box = driver.find_element(by=By.NAME,value="username")
username_box.send_keys(val_StudentNum)
password_box = driver.find_element(by=By.ID,value="password")
password_box.send_keys(val_passWord)
click_button = driver.find_element(by=By.ID, value = "submit-button")
print("================loging...")
click_button.click()
driver.implicitly_wait(5)

while (True):
    signDay(val_month_iter,val_day_iter)
    val_month_iter = val_month_iter+1 if doMonthAddAdjust(val_month_iter,val_day_iter) else val_month_iter
    val_day_iter = 1 if doMonthAddAdjust(val_month_iter,val_day_iter) else val_day_iter+1
    if(val_month_iter == val_month_end and val_day_iter == val_day_end):
        break
    pass
signDay(val_month_end,val_day_end)

driver.implicitly_wait(5)
print("================halt")
input()
driver.quit()

