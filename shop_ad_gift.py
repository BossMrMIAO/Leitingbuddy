import time
import pyautogui
from pyautogui import ImageNotFoundException
from logger import logger
from ad_watch_until_end import ad_watch_until_end_by_location


def shop_ad_gift():
    # 点击商店
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/shop.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击商店")
    # 点击视频广告按钮
    First_while = True
    while First_while == True:
        try:
            time.sleep(2)
            location = pyautogui.locateOnWindow('shop_ad_gift/shop_ad_video.png', '雷霆战机：集结', confidence=0.8)
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
            location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
            time.sleep(2)
            pyautogui.click(location)
            logger.info('返回主界面')
            First_while = False
