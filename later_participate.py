import time
import pyautogui
from pyautogui import ImageNotFoundException
from logger import logger

def later_participate(second_while = True):
    # 自动弹出
    while second_while:
        try:
            time.sleep(2)
            location = pyautogui.locateOnWindow('assets/special/later_participate.png', '雷霆战机：集结', confidence=0.8)
            pyautogui.click(location)
        except ImageNotFoundException:
            logger.info("稍后参与按钮未出现，继续原流程")
            second_while = False
            # pyautogui.click()