
import pyautogui
import time
from later_participate import later_participate

def login():
    # 点击启动软件
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/leiting_logo.png', confidence=0.8)
    pyautogui.doubleClick(location)
    # 等待登录按钮出现
    time.sleep(10)
    # 点击登录
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/login.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    # 等待登陆成功
    time.sleep(10)
    later_participate(second_while = True)