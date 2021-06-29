from selenium import webdriver
from winsound import Beep as bp
import time
import datetime
import calendar
from segmented_display import L, time_table
import pyautogui
from selenium.webdriver.common.keys import Keys

x = webdriver.Chrome(executable_path="D:\Webdriver\chromedriver.exe")
bp(1000, 300)


def beep(x):
    for i in range(2):
        bp(1000, 500)
        time.sleep(x)


uid = "20BCS4069"
cuims_pass = "Chirag@123456"
BB_pass = "Chirag@1234"


def login_cuims():
    global uid, cuims_pass
    week_day = {'Monday': 3, 'Tuesday': 4, 'Wednesday': 5, 'Thursday': 6, 'Friday': 7, 'Saturday': 8}
    class_timing = {'10:00': 3, '11:00': 4, '12:00': 5, '12:45': 6, '01:45': 7, '02:45': 8}

    x = webdriver.Chrome(executable_path="D:\Webdriver\chromedriver.exe")
    x.get("https://uims.cuchd.in/uims/")

    bp(1000, 300)
    x.maximize_window()
    # open cuims and enter password
    while True:
        try:
            x.find_element_by_xpath('/html/body/form/div[3]/div/div/div[2]/div/input[1]').send_keys(uid)
            x.find_element_by_xpath('/html/body/form/div[3]/div/div/div[2]/div/input[2]').click()
            x.find_element_by_xpath('/html/body/form/div[3]/div/div/div[2]/div/input[1]').send_keys(cuims_pass)
            x.find_element_by_xpath('/html/body/form/div[3]/div/div/div[2]/div/input[2]').click()
            break
        except:
            beep(2)

    a = 1

    while True:
        time.sleep(2)
        try:
            x.find_element_by_xpath('/html/body/form/div[4]/header/div[1]/div').click()
            time.sleep(1)
            x.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/ul/li[1]/a').click()
            time.sleep(1)
            x.find_element_by_xpath('/html/body/form/div[4]/div[1]/div/div[1]/ul/ul[1]/li[5]/a').click()
            break
        except:
            a += 1
            if a >= 3:
                x.quit()
                return time_table
            beep(2)
    a = 1
    while True:
        time.sleep(3)
        try:
            x.find_element_by_xpath(
                '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[3]/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/div')
            break
        except:
            a += 1
            if a >= 3:
                x.quit()
                return time_table
            beep(2)

    for i in week_day:

        timing_copy = {'10:00': 3, '11:00': 4, '12:00': 5, '12:45': 6, '01:45': 7, '02:45': 8}
        for j in class_timing:
            day = week_day[i]
            timing = class_timing[j]

            try:
                txt = (
                        '/html/body/form/div[4]/div[3]/div/table/tbody/tr[3]/td/span/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[3]/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[%(j)s]/td[%(i)s]/div' % {
                    'i': day, 'j': timing})

                which_class = x.find_element_by_xpath(txt).text
                timing_copy[j] = L[which_class[0:9]]

            except:
                timing_copy[j] = ''
                continue

        week_day[i] = timing_copy

    bp(1000, 300)
    x.quit()
    return week_day


def write_timetable():
    def add(x, y):
        y.write(f"'{x}'")

    with open('Time_Table.py', 'w') as f:
        f.write("time_table = {")
        for i in time_table:
            add(i, f)
            f.write(" : {\n")
            for j in i:
                add(j, f)
            f.write("hi")


def login_blackboard(enter_class):
    global x, uid, BB_pass
    x.get("https://cuchd.blackboard.com/")
    bp(1000, 300)
    x.maximize_window()
    while True:
        try:
            x.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div/div/div[2]/button').click()
            x.find_element_by_xpath('/html/body/div[2]/div[1]/div/form/div/ul/li[1]/input').send_keys(uid)
            time.sleep(0.1)
            x.find_element_by_xpath('/html/body/div[2]/div[1]/div/form/div/ul/li[2]/input').send_keys(BB_pass)
            x.find_element_by_xpath('/html/body/div[2]/div[1]/div/form/div/ul/li[3]/input').click()
            break
        except:
            beep(2)
    bp(1000, 300)
    while True:
        try:
            class_bb = x.find_element_by_xpath("/html/body/div[1]/div[2]/bb-base-layout/div/main/div")
            class_bb.send_keys(Keys.DOWN)

            time.sleep(1)
            x.find_element_by_xpath(enter_class).click()
            break
        except:
            pass

    bp(1000, 300)
    while True:
        time.sleep(2)
        try:
            time.sleep(1)
            x.find_element_by_xpath(
                '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/aside/div[6]/div[2]/div[2]/div/div/button/span').click()
            x.find_element_by_xpath(
                '/html/body/div[1]/div[2]/bb-base-layout/div/main/div[3]/div/div[3]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/aside/div[6]/div[2]/div[2]/div/div/ul/li[2]/a').click()
            bp(1000, 300)
            break
        except:
            pass


today = calendar.day_name[datetime.date.today().weekday()]
hour = time.strftime("%I", time.localtime())
minute = time.strftime("%M", time.localtime())
start_p = 0
start_time = 20

def start_class(s):
    i_0 = s[today]
    for i in i_0:
        if abs(60 * int(hour) + int(minute) - 60 * int(i[0:2]) - int(i[3:6])) < start_time:
            if i_0[i] == '':
                beep(2)
                x.close()
                # msg = pyautogui.confirm("I Checked There Was No Class!!", 'Error Message', buttons=["Ok"])
                exit()
                break
            else:
                login_blackboard(enter_class=i_0[i])
        else:
            continue
    else:
        # msg = pyautogui.confirm("I Checked There Was No Class!!", 'Error Message', buttons=["Ok"])
        exit()


if start_p == 0:
    s = login_cuims()
    start_class(s)
else:
    s = time_table
    start_class(s)
