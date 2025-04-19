import time
import pyautogui
from pyautogui import ImageNotFoundException
from logger import logger
from ad_watch_until_end import ad_watch_until_end_by_location

def find_chest(second_while = True):
    # 点击寻宝
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/find_chest/find_chest.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    # 检查宝箱按钮
    time.sleep(2)
    while second_while:
        try:
            time.sleep(2)
            location = pyautogui.locateOnWindow('assets/find_chest/find_chest_ad_video.png', '雷霆战机：集结', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击看寻宝视频广告")
            ad_watch_until_end_by_location()
            # 开宝箱
            time.sleep(2)
            location = pyautogui.locateOnWindow('assets/find_chest/chest.png', '雷霆战机：集结', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击开宝箱")
            # 领取奖励
            time.sleep(2)
            location = pyautogui.locateOnWindow('assets/get_chest.png', '雷霆战机：集结', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击领取奖励")
        except ImageNotFoundException:
            logger.info("宝箱视频广告按钮未出现，继续原流程")
            second_while = False
    # 点击返回
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击返回")