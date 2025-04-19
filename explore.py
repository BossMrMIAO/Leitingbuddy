import time
import pyautogui
from pyautogui import ImageNotFoundException
from logger import logger
from ad_watch_until_end import ad_watch_until_end_by_location


def explore():
    # 点击星际探索
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/explore.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info('点击星际探索')
    # 点击快速探索
    try:
        time.sleep(2)
        location = pyautogui.locateOnWindow('assets/quick_explore.png', '雷霆战机：集结', confidence=0.8)
        pyautogui.click(location)
        logger.info('点击快速探索')
        # 检查是否有首次免看广告领取
        try:
            time.sleep(2)
            location = pyautogui.locateOnWindow('explore/explore_first_no_ad.png', '雷霆战机：集结', confidence=0.8)
            pyautogui.click(location)
            logger.info('点击首次免看广告领取')
            # 领取奖励
            time.sleep(2)
            congratulations_location = pyautogui.locateOnWindow('assets/congratulations.png', '雷霆战机：集结', confidence=0.8)
            get_chest_location = pyautogui.locateOnWindow('assets/get_chest.png', '雷霆战机：集结', confidence=0.8)
            time.sleep(2)
            pyautogui.click(get_chest_location)
            logger.info("首次免费奖励领取")
        except ImageNotFoundException:
            logger.info('没有首次免看广告领取')  
    except ImageNotFoundException:
        logger.info('没有快速探索')
        time.sleep(5)
        location = pyautogui.locateOnWindow('assets/close_explore.png', '雷霆战机：集结', confidence=0.8)
        time.sleep(2)
        pyautogui.click(location)
        logger.info('关闭探索')
        return
    # 点击视频广告按钮
    first_while = True
    while first_while:
        try:
            time.sleep(2)
            location = pyautogui.locateOnWindow('explore/explore_ad_video.png', '雷霆战机：集结', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击视频广告按钮")
            # 监听广告看完情况，点击关闭界面，复活成功
            second_while = True
            ad_watch_until_end_by_location()

            time.sleep(2)
            congratulations_location = pyautogui.locateOnWindow('assets/congratulations.png', '雷霆战机：集结', confidence=0.8)
            get_chest_location = pyautogui.locateOnWindow('assets/get_chest.png', '雷霆战机：集结', confidence=0.8)
            time.sleep(2)
            pyautogui.click(get_chest_location)
            logger.info("奖励领取")
        except ImageNotFoundException:
            logger.info("没广告可看了")
            time.sleep(5)
            location = pyautogui.locateOnWindow('assets/close_explore.png', '雷霆战机：集结', confidence=0.8)
            time.sleep(2)
            pyautogui.click(location)
            logger.info('关闭探索')
            first_while = False