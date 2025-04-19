import time
import pyautogui
from pyautogui import ImageNotFoundException
from logger import logger
from ad_watch_until_end import ad_watch_until_end_by_location


def endless_mode(
        close_app_after_chest_full = True,
        buddy_help_enable_flag=True,
        endless_selection = 'world_challenge'
):
    # 初始化循环控制变量
    challenge_coin_full = False
    chest_full = False
    # 点击无尽模式
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/endless/endless_mode.png', '雷霆战机：集结', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击无尽模式")
    while True:
        if endless_selection == 'world_challenge':
            # 点击世界挑战
            time.sleep(2)
            location = pyautogui.locateOnWindow('assets/endless/world_challenge.png', '雷霆战机：集结', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击世界挑战")
            # 挑战币没满，继续
            if challenge_coin_full == False:
                # 点击金币场
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/endless/world_gold_field.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击金币场")

                # 检查挑战币是否已满，从提示的角度获取挑战币状态
                try:
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/endless/world_challenge_coin_full_cancel.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("今日挑战币已满的提示，点击后下次不会触发窗口, 转头去打好友竞赛")
                    challenge_coin_full = True
                    # 点击返回
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("点击返回到好友竞赛和世界竞赛选择界面")
                except ImageNotFoundException:
                    logger.info("未触发挑战币已满的窗口，不知道挑战币是否满了，继续原流程")
                    # 取消助战选项
                    if not buddy_help_enable_flag:
                        time.sleep(2)
                        location = pyautogui.locateOnWindow('assets/endless/buddy_help_enable.png', '雷霆战机：集结', confidence=0.8)
                        pyautogui.click(location)
                        logger.info("取消助战选项")
                    # 点击助战出击
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/endless/go.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("点击助战出击")
                    # 点击匹配,当前在祝福界面
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/endless/world_match.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("点击匹配,当前在祝福界面")
                    # 检测爆弹图标，以表明匹配完成
                    while True:
                        try:
                            time.sleep(5)
                            location = pyautogui.locateOnWindow('assets/base/bomb.png', '雷霆战机：集结', confidence=0.8)
                            logger.info("检测到爆弹图标，匹配完成")
                            break
                        except ImageNotFoundException:
                            logger.info("没有爆弹图标，匹配未完成")
                    # 监听死亡界面，等待复活按钮出现
                    avoid_missile = 0
                    while True:
                        try:
                            time.sleep(2)
                            revive_location = pyautogui.locateOnWindow('assets/revive.png', '雷霆战机：集结', confidence=0.8)
                            break
                        except ImageNotFoundException:
                            logger.info("等待复活按钮出现")
                            avoid_missile = avoid_missile + 1
                            # 开局30s后向右移动一点，躲避导弹
                            if avoid_missile == 3:
                                logger.info('开始移动到躲避导弹位置')
                                # 单击起始位置
                                pyautogui.click()
                                # 定义相对拖拽的距离
                                relative_x = 50
                                relative_y = 0
                                # 模拟按下鼠标左键并进行相对拖拽，duration 参数控制拖拽的持续时间
                                pyautogui.dragRel(relative_x, relative_y, duration=1)
                            time.sleep(5)
                    # 点击复活按钮, 看广告
                    pyautogui.click(revive_location)
                    logger.info("点击复活按钮, 看广告")
                    # 监听广告看完情况，点击关闭界面，复活成功
                    ad_watch_until_end_by_location()
                    # 第二次死亡，这次没有广告可看了，结束战斗
                    avoid_missile = 0
                    while True:
                        try:
                            time.sleep(2)
                            revive_40_diamond_location = pyautogui.locateOnWindow('assets/revive_40_diamond.png', '雷霆战机：集结', confidence=0.8)
                            break
                        except ImageNotFoundException:
                            logger.info("等待二次死亡")
                            avoid_missile = avoid_missile + 1
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
                            time.sleep(5)
                    exit_battle_location = pyautogui.locateOnWindow('assets/exit_battle.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(exit_battle_location)
                    time.sleep(5)
                    logger.info("战斗结束")
                    # 结算界面，可能有宝箱开
                    try:
                        time.sleep(2)
                        congratulations_location = pyautogui.locateOnWindow('assets/congratulations.png', '雷霆战机：集结', confidence=0.8)
                        get_chest_location = pyautogui.locateOnWindow('assets/get_chest.png', '雷霆战机：集结', confidence=0.8)
                        time.sleep(2)
                        pyautogui.click(get_chest_location)
                        logger.info("结算界面，有宝箱开")
                    except ImageNotFoundException:
                        # 没有箱子开
                        logger.info("没有箱子开, 今日宝箱已满")
                        chest_full = True
                    # 结算界面，领取完毕宝箱或没有箱子，检查有没有挑战币
                    try:
                        time.sleep(2)
                        location = pyautogui.locateOnWindow('assets/endless/challenge_coin.png', '雷霆战机：集结', confidence=0.8)
                        logger.info("结算界面，有挑战币")
                    except ImageNotFoundException:
                        # 没有挑战币图标了
                        logger.info("没有挑战币了，今日挑战币已满")
                        challenge_coin_full = True
                    # 结算界面，点击继续
                    time.sleep(2)
                    continue_location = pyautogui.locateOnWindow('assets/continue.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(continue_location)
                    # 对手与我比较界面，对手可能打完或没打完, 都点击返回，会停留在世界竞赛选赛场界面
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("对手与我比较界面, 无论输赢，点击返回")
                    # 返回到好友竞赛和世界竞赛选择界面
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("返回到好友竞赛和世界竞赛选择界面")
            else:
                # 挑战币满了，去打好友竞赛
                endless_selection = 'friend_competition'
                # 箱子没打光，返回到切换好友竞赛和世界竞赛界面
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("返回到切换好友竞赛和世界竞赛界面")
                # 如果箱子也打光了，直接回到首页
                if chest_full == True:
                    # 返回到首页
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("返回到首页")
                    # 如果检测到了无尽小组赛结算，把奖励领了
                    try:
                        time.sleep(5)
                        location = pyautogui.locateOnWindow('assets/special/special_competition_reward.png', '雷霆战机：集结', confidence=0.8)
                        pyautogui.click(location)
                        logger.info("检测到无尽小组赛结算，把奖励领了")
                        # 领取奖励
                        time.sleep(5)
                        location = pyautogui.locateOnWindow('assets/get_chest.png', '雷霆战机：集结', confidence=0.8)
                        pyautogui.click(location)
                        logger.info("领取奖励")
                    except ImageNotFoundException:
                        logger.info("没有检测到无尽小组赛结算，跳过领取奖励")
                    if close_app_after_chest_full:
                        # 点击关闭软件
                        time.sleep(2)
                        location = pyautogui.locateOnWindow('assets/close_app.png', '雷霆战机：集结', confidence=0.8)
                        pyautogui.click(location)
                        logger.info("点击关闭软件")
                    # 循环直接结束了
                    break
     
        else:
            # 好友竞赛
            # 检查宝箱是否已满
            if chest_full == False:
                # 宝箱没满，继续
                # 点击好友竞赛
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/endless/friend_competition.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击好友竞赛")
                # 取消助战选项
                if not buddy_help_enable_flag:
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/endless/buddy_help_enable.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("取消助战选项")
                # 点击出击
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/endless/go.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击出击")
                # 点击出击,当前在祝福界面
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/endless/go.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击出击,当前在祝福界面")
                # 监听死亡界面，等待复活按钮出现
                avoid_missile = 0
                while True:
                    try:
                        time.sleep(2)
                        revive_location = pyautogui.locateOnWindow('assets/revive.png', '雷霆战机：集结', confidence=0.8)
                        break
                    except ImageNotFoundException:
                        logger.info("等待复活按钮出现")
                        avoid_missile = avoid_missile + 1
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
                        time.sleep(5)
                # 点击复活按钮, 看广告
                pyautogui.click(revive_location)
                logger.info("点击复活按钮, 看广告")
                # 监听广告看完情况，点击关闭界面，复活成功
                ad_watch_until_end_by_location()

                # 第二次死亡，这次没有广告可看了，结束战斗
                avoid_missile = 0
                while True:
                    try:
                        time.sleep(2)
                        revive_40_diamond_location = pyautogui.locateOnWindow('assets/revive_40_diamond.png', '雷霆战机：集结', confidence=0.8)
                        break
                    except ImageNotFoundException:
                        logger.info("等待二次死亡")
                        avoid_missile = avoid_missile + 1
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
                        time.sleep(5)
                exit_battle_location = pyautogui.locateOnWindow('assets/exit_battle.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(exit_battle_location)
                time.sleep(5)
                logger.info("战斗结束")
                # 结算界面，可能有宝箱开
                try:
                    time.sleep(2)
                    congratulations_location = pyautogui.locateOnWindow('assets/congratulations.png', '雷霆战机：集结', confidence=0.8)
                    get_chest_location = pyautogui.locateOnWindow('assets/get_chest.png', '雷霆战机：集结', confidence=0.8)
                    time.sleep(2)
                    pyautogui.click(get_chest_location)
                    logger.info("结算界面，有宝箱开")
                except ImageNotFoundException:
                    # 没有箱子开
                    logger.info("没有箱子开，结束了")
                    chest_full = True
                # 结算界面，点击继续,会跳转到好友竞赛和世界竞赛选择界面
                time.sleep(2)
                continue_location = pyautogui.locateOnWindow('assets/continue.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(continue_location)
                logger.info("点击继续，跳转到好友竞赛和世界竞赛选择界面")
            else:
                # 宝箱满了，而且世界竞赛也打完了，返回首页后关闭
                # 返回到首页
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("返回到首页")
                # 如果检测到了无尽小组赛结算，把奖励领了
                try:
                    time.sleep(5)
                    location = pyautogui.locateOnWindow('assets/special/special_competition_reward.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("检测到无尽小组赛结算，把奖励领了")
                    # 领取奖励
                    time.sleep(5)
                    location = pyautogui.locateOnWindow('assets/get_chest.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("领取奖励")
                except ImageNotFoundException:
                    logger.info("没有检测到无尽小组赛结算，跳过领取奖励")
                if close_app_after_chest_full:
                    # 点击关闭软件
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/close_app.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("点击关闭软件")
                # 循环直接结束了
                break
