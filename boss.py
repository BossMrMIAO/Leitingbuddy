import time
import pyautogui
from pyautogui import ImageNotFoundException
from logger import logger
from ad_watch_until_end import ad_watch_until_end_by_location

def boss():
    # 闯关
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/standard/standard_entrance.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击闯关")
    # 点击boss
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/boss/boss.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击boss")
    # 点击第一个要打的boss, 本次闪击3次
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/boss/tianma_plane.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击第一个要打的boss")
    # 闪击3次
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/boss/pre_lightning_battle.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击预定闪击")
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/boss/lightning_battle.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击闪击")
    # 确认
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/boss/confirm.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击确定")
    # 等待战斗结束和结算<TODO>

    # 返回
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击返回")
    # 点击第二个要打的boss, 本次只打一次
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/boss/xiannv_wingman.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击第二个要打的boss")
    # 单次战斗
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/boss/single_battle.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击单次战斗")
    # 确定
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/boss/confirm.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击确定")
    # 等待战斗结束和结算<TODO>

    # 连续3次点击返回
    for i in range(3):
        time.sleep(2)
        location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
        pyautogui.click(location)
        logger.info("点击返回")