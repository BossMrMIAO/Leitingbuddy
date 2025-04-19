import time
import pyautogui
from pyautogui import ImageNotFoundException
from logger import logger
from ad_watch_until_end import ad_watch_until_end_by_location

def energy_buy(ad_video_buy_count = 4):
    # 点击能量购买页面
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/energy/energy_buy.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info('点击体力购买页面')
    # 开始看广告免费买体力
    while ad_video_buy_count > 0:
        try:
            time.sleep(2)
            location = pyautogui.locateOnWindow('assets/energy/energy_buy_ad_video.png', '雷霆战机：集结', confidence=0.98)
            pyautogui.click(location)
            logger.info("点击视频广告按钮")
            ad_watch_until_end_by_location()
            ad_video_buy_count = ad_video_buy_count - 1
        except ImageNotFoundException:
            logger.info("没广告可看了")
            first_while = False
    # 免费体力拿完了
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/energy/close_energy_buy.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)