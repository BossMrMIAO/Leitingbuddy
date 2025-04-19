import time
import pyautogui
from pyautogui import ImageNotFoundException
from logger import logger
from ad_watch_until_end import ad_watch_until_end_by_location


def battle_stage(mode = 'endless'):
    # 监听死亡界面，等待复活按钮出现
    wait_revive = True
    avoid_missile = 0
    while wait_revive:
        try:
            time.sleep(2)
            revive_location = pyautogui.locateOnWindow('assets/revive.png', '雷霆战机：集结', confidence=0.8)
            break
        except ImageNotFoundException:
            logger.info("等待复活按钮出现")
            avoid_missile = avoid_missile + 1
            if mode == 'endless':
                # 开局30s后向右移动一点，躲避导弹
                if avoid_missile == 4:
                    logger.info('开始移动到躲避导弹位置')
                    # 单击起始位置
                    pyautogui.click()
                    # 定义相对拖拽的距离
                    relative_x = 50
                    relative_y = 0
                    # 模拟按下鼠标左键并进行相对拖拽，duration 参数控制拖拽的持续时间
                    pyautogui.dragRel(relative_x, relative_y, duration=1)
            elif mode == 'standard':
                # 一直没有复活按钮也可能是胜利了, 闯关模式下，胜利必给钥匙
                try:
                    location = pyautogui.locateOnWindow('assets/standard/key.png', '雷霆战机：集结', confidence=0.8)
                    logger.info("胜利了")
                    wait_revive = False
                except ImageNotFoundException:
                    logger.info("闯关模式暂时没有胜利")
            time.sleep(5)
    if wait_revive:
        # 点击复活按钮, 看广告
        pyautogui.click(revive_location)
        logger.info("点击复活按钮, 看广告")
        # 监听广告看完情况，点击关闭界面，复活成功
        ad_watch_until_end_by_location()

    # 第二次死亡，这次没有广告可看了，结束战斗
    avoid_missile = 0
    while wait_revive:
        try:
            time.sleep(2)
            revive_40_diamond_location = pyautogui.locateOnWindow('assets/revive_40_diamond.png', '雷霆战机：集结', confidence=0.8)
            break
        except ImageNotFoundException:
            logger.info("等待二次死亡")
            avoid_missile = avoid_missile + 1
            if mode == 'endless':
                # 开局30s后向右移动一点，躲避导弹
                if avoid_missile == 2:
                    logger.info('开始移动到躲避导弹位置')
                    # 单击起始位置
                    pyautogui.click()
                    # 定义相对拖拽的距离
                    relative_x = 50
                    relative_y = 0
                    # 模拟按下鼠标左键并进行相对拖拽，duration 参数控制拖拽的持续时间
                    pyautogui.dragRel(relative_x, relative_y, duration=1)
            elif mode == 'standard':
                # 一直没有复活按钮也可能是胜利了, 闯关模式下，胜利必给钥匙
                try:
                    location = pyautogui.locateOnWindow('assets/standard/key.png', '雷霆战机：集结', confidence=0.8)
                    logger.info("胜利了")
                    wait_revive = False
                except ImageNotFoundException:
                    logger.info("闯关模式暂时没有胜利")
            time.sleep(5)
    if wait_revive:
        exit_battle_location = pyautogui.locateOnWindow('assets/exit_battle.png', '雷霆战机：集结', confidence=0.8)
        pyautogui.click(exit_battle_location)
        time.sleep(5)
        logger.info("战斗结束")
    # # 结算界面，可能有宝箱开
    # try:
    #     time.sleep(2)
    #     congratulations_location = pyautogui.locateOnWindow('assets/congratulations.png', '雷霆战机：集结', confidence=0.8)
    #     get_chest_location = pyautogui.locateOnWindow('assets/get_chest.png', '雷霆战机：集结', confidence=0.8)
    #     time.sleep(2)
    #     pyautogui.click(get_chest_location)
    #     logger.info("结算界面，有宝箱开")
    # except ImageNotFoundException:
    #     # 没有箱子开
    #     logger.info("没有箱子开")
    #     time.sleep(2)
    #     if mode == 'endless':
    #         location = pyautogui.locateOnWindow('assets/close_app.png', '雷霆战机：集结', confidence=0.8)
    #         time.sleep(2)
    #         pyautogui.click(location)
    #     time.sleep(2)

    # 结算界面，点击继续
    time.sleep(2)
    if mode != 'endless':
        try:
            location = pyautogui.locateOnWindow('assets/battle_fail.png', '雷霆战机：集结', confidence=0.8)
            battle_victory = False
        except ImageNotFoundException:
            battle_victory = True
            # 检查是否有双倍奖励按钮
            try:
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/standard/ad_double_reward.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击双倍奖励")
                ad_watch_until_end_by_location()
            except ImageNotFoundException:
                logger.info("没有双倍奖励")
    time.sleep(2)
    continue_location = pyautogui.locateOnWindow('assets/continue.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(continue_location)
    # 返回战斗结果
    return battle_victory