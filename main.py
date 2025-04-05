import pyautogui
import time
import cv2
import numpy as np
import pygetwindow as gw
import pytesseract
from PIL import Image
import logging
import coloredlogs

# 创建 Logger 对象并配置
logger = logging.getLogger(__name__)
coloredlogs.install(
    level='DEBUG',  # 设置最低日志级别
    logger=logger,
    fmt='%(asctime)s [%(levelname)s] %(message)s',  # 时间+级别+信息
    datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式
    level_styles={
        'info': {'color': 'green', 'bold': True},
        'warning': {'color': 'yellow', 'bright': True},
        'error': {'color': 'red', 'background': 'white'}
    }
)


def find_chest(second_while = True):
    # 点击寻宝
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/find_chest/find_chest.png', confidence=0.8)
    pyautogui.click(location)
    # 检查宝箱按钮
    time.sleep(2)
    while second_while:
        try:
            time.sleep(2)
            location = pyautogui.locateOnScreen('assets/find_chest/find_chest_ad_video.png', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击看寻宝视频广告")
            ad_watch_until_end()
            # 开宝箱
            time.sleep(2)
            location = pyautogui.locateOnScreen('assets/find_chest/chest.png', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击开宝箱")
            # 领取奖励
            time.sleep(2)
            location = pyautogui.locateOnScreen('assets/get_chest.png', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击领取奖励")
        except:
            logger.info("宝箱视频广告按钮未出现，继续原流程")
            second_while = False
    # 点击返回
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击返回")


def boss():
    # 闯关
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/standard/standard_entrance.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击闯关")
    # 点击boss
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/boss/boss.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击boss")
    # 点击第一个要打的boss, 本次闪击3次
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/boss/tianma_plane.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击第一个要打的boss")
    # 闪击3次
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/boss/pre_lightning_battle.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击预定闪击")
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/boss/lightning_battle.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击闪击")
    # 确认
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/boss/confirm.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击确定")
    # 等待战斗结束和结算<TODO>

    # 返回
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击返回")
    # 点击第二个要打的boss, 本次只打一次
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/boss/xiannv_wingman.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击第二个要打的boss")
    # 单次战斗
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/boss/single_battle.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击单次战斗")
    # 确定
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/boss/confirm.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击确定")
    # 等待战斗结束和结算<TODO>

    # 连续3次点击返回
    for i in range(3):
        time.sleep(2)
        location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
        pyautogui.click(location)
        logger.info("点击返回")




def later_participate(second_while = True):
    # 自动弹出
    while second_while:
        try:
            time.sleep(2)
            location = pyautogui.locateOnScreen('assets/special/later_participate.png', confidence=0.8)
            pyautogui.click(location)
        except:
            logger.info("稍后参与按钮未出现，继续原流程")
            second_while = False
            # pyautogui.click()


def login():
    # 点击启动软件
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/leiting_logo.png', confidence=0.8)
    pyautogui.doubleClick(location)
    # 等待登录按钮出现
    time.sleep(10)
    # 点击登录
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/login.png', confidence=0.8)
    pyautogui.click(location)
    # 等待登陆成功
    time.sleep(10)
    later_participate(second_while = True)

def process_image(image):
    """
    将图像转换为灰度图并进行二值化处理，提取白色文字
    :param image: PIL 图像对象
    :return: 二值化后的 OpenCV 图像
    """
    # 将 PIL 图像转换为 OpenCV 格式
    open_cv_image = np.array(image)
    # 转换为 HSV 颜色空间
    hsv = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2HSV)

    # 定义白色的 HSV 范围
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 30, 255])

    # 创建掩码，只保留白色部分
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # 将掩码应用到原始图像
    result = cv2.bitwise_and(open_cv_image, open_cv_image, mask=mask)

    # 转换为灰度图
    gray = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)

    # 进行二值化处理
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # # 显示处理后的图像
    # cv2.imshow('Processed Image', result)
    # cv2.waitKey(0)  # 等待按键事件
    # cv2.destroyAllWindows()  # 关闭所有窗口
    return binary

def ad_watch_until_end(second_while = True):
    direct_close_counter = 10
    # 读取参考图标
    reference_image = Image.open('assets/ad/ad_end.png')
    reference_ad_close_image = Image.open('assets/ad/close_ad.png')
    # 对参考图标进行预处理
    processed_reference = process_image(reference_image)
    processed_reference_ad_close = process_image(reference_ad_close_image)
    # 监听广告看完情况，点击关闭界面，复活成功
    while second_while:
        time.sleep(2)
        if direct_close_counter != 0 :
            # 截取屏幕
            screenshot = pyautogui.screenshot()
            # 对屏幕截图进行预处理
            processed_screenshot = process_image(screenshot)
            # 使用 OpenCV 进行模板匹配
            result = cv2.matchTemplate(processed_screenshot, processed_reference, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            # 匹配到的区域，然后重新匹配关闭按钮的区域，并且匹配到之后点击关闭它
            if max_val >= 0.9:
                result = cv2.matchTemplate(processed_screenshot, processed_reference_ad_close, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                h, w = processed_reference_ad_close.shape
                top_left = max_loc
                center = (top_left[0] + w // 2, top_left[1] + h // 2)
                close_ad_location = center
                # 点击定位到的位置
                logger.info(f'要点击的位置是{center}')
                pyautogui.click(close_ad_location)
                logger.info("成功检测到目标元素并尝试关闭广告")
                try:
                    time.sleep(0.5)
                    location = pyautogui.locateOnScreen('assets/ad/continue_ad.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("广告关闭不成功，继续看完广告")
                except:
                    logger.info("广告关闭成功，复活成功")
                    second_while = False
            else:
                close_ad_location = None
                logger.info(f"未找到目标元素，剩余强制点击关闭的倒计数：{direct_close_counter}")
                direct_close_counter = direct_close_counter - 1
                time.sleep(5)

        else:
            # 超时的操作，看来没有定位到已看完广告，改为直接定位关闭按钮，然后直接关闭，直接点击关闭尝试
            logger.info('本次是检查关闭按钮，并点击关闭')
            result = cv2.matchTemplate(processed_screenshot, processed_reference_ad_close, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            h, w = processed_reference_ad_close.shape
            top_left = max_loc
            center = (top_left[0] + w // 2, top_left[1] + h // 2)
            close_ad_location = center
            # 点击定位到的位置
            logger.info(f'要点击的位置是{center}')
            pyautogui.click(close_ad_location)
            logger.info("成功检测到目标元素并尝试关闭广告，强制点击时广告应该早就看完了")
            try:
                time.sleep(0.5)
                location = pyautogui.locateOnScreen('assets/ad/continue_ad.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("广告关闭不成功，继续看完广告")
            except:
                logger.info("广告关闭成功与否也不知道，我就当他成功了，继续往下走了")
                second_while = False




                # ad_end_location = pyautogui.locateOnScreen('assets/ad/ad_end.png', confidence=0.8)
            # direct_close_counter = 8
            # time.sleep(2)
            # close_ad_location = pyautogui.locateOnScreen('assets/ad/close_ad.png', confidence=0.5)
            # pyautogui.click(close_ad_location)
            # try:
            #     time.sleep(0.5)
            #     location = pyautogui.locateOnScreen('assets/ad/continue_ad.png', confidence=0.8)
            #     pyautogui.click(location)
            #     logger.info("广告关闭不成功，继续看完广告")
            # except:
            #     logger.info("广告关闭成功，复活成功")
            #     second_while = False


def endless_mode(close_app_after_chest_full = True,endless_selection = 'world_challenge'):
    # 初始化循环控制变量
    challenge_coin_full = False
    chest_full = False
    # 点击无尽模式
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/endless/endless_mode.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击无尽模式")
    while True:
        if endless_selection == 'world_challenge':
            # 点击世界挑战
            time.sleep(2)
            location = pyautogui.locateOnScreen('assets/endless/world_challenge.png', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击世界挑战")
            # 挑战币没满，继续
            if challenge_coin_full == False:
                # 点击金币场
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/endless/world_gold_field.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击金币场")

                # 检查挑战币是否已满，从提示的角度获取挑战币状态
                try:
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/endless/world_challenge_coin_full_cancel.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("今日挑战币已满的提示，点击后下次不会触发窗口, 转头去打好友竞赛")
                    challenge_coin_full = True
                    # 点击返回
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("点击返回到好友竞赛和世界竞赛选择界面")
                except:
                    logger.info("未触发挑战币已满的窗口，不知道挑战币是否满了，继续原流程")
                    # 点击助战出击
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/endless/go.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("点击助战出击")
                    # 点击匹配,当前在祝福界面,
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/endless/world_match.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("点击匹配,当前在祝福界面")
                    # 检测爆弹图标，以表明匹配完成
                    while True:
                        try:
                            time.sleep(5)
                            location = pyautogui.locateOnScreen('assets/base/bomb.png', confidence=0.8)
                            logger.info("检测到爆弹图标，匹配完成")
                            break
                        except:
                            logger.info("没有爆弹图标，匹配未完成")
                    # 监听死亡界面，等待复活按钮出现
                    avoid_missile = 0
                    while True:
                        try:
                            time.sleep(2)
                            revive_location = pyautogui.locateOnScreen('assets/revive.png', confidence=0.8)
                            break
                        except:
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
                    ad_watch_until_end(second_while=True)
                    # 第二次死亡，这次没有广告可看了，结束战斗
                    avoid_missile = 0
                    while True:
                        try:
                            time.sleep(2)
                            revive_40_diamond_location = pyautogui.locateOnScreen('assets/revive_40_diamond.png', confidence=0.8)
                            break
                        except:
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
                    exit_battle_location = pyautogui.locateOnScreen('assets/exit_battle.png', confidence=0.8)
                    pyautogui.click(exit_battle_location)
                    time.sleep(5)
                    logger.info("战斗结束")
                    # 结算界面，可能有宝箱开
                    try:
                        time.sleep(2)
                        congratulations_location = pyautogui.locateOnScreen('assets/congratulations.png', confidence=0.8)
                        get_chest_location = pyautogui.locateOnScreen('assets/get_chest.png', confidence=0.8)
                        time.sleep(2)
                        pyautogui.click(get_chest_location)
                        logger.info("结算界面，有宝箱开")
                    except:
                        # 没有箱子开
                        logger.info("没有箱子开, 今日宝箱已满")
                        chest_full = True
                    # 结算界面，领取完毕宝箱或没有箱子，检查有没有挑战币
                    try:
                        time.sleep(2)
                        location = pyautogui.locateOnScreen('assets/endless/challenge_coin.png', confidence=0.8)
                        logger.info("结算界面，有挑战币")
                    except:
                        # 没有挑战币图标了
                        logger.info("没有挑战币了，今日挑战币已满")
                        challenge_coin_full = True
                    # 结算界面，点击继续
                    time.sleep(2)
                    continue_location = pyautogui.locateOnScreen('assets/continue.png', confidence=0.8)
                    pyautogui.click(continue_location)
                    # 对手与我比较界面，对手可能打完或没打完, 都点击返回，会停留在世界竞赛选赛场界面
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("对手与我比较界面, 无论输赢，点击返回")
                    # 返回到好友竞赛和世界竞赛选择界面
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("返回到好友竞赛和世界竞赛选择界面")
            else:
                # 挑战币满了，去打好友竞赛
                endless_selection = 'friend_competition'
                # 如果箱子也打光了，直接回到首页
                if chest_full == True:
                    # 返回到好友竞赛与世界竞赛选择界面
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("返回到好友竞赛与世界竞赛选择界面")
                    # 返回到首页
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("返回到首页")
                    if close_app_after_chest_full:
                        # 点击关闭软件
                        time.sleep(2)
                        location = pyautogui.locateOnScreen('assets/close_app.png', confidence=0.8)
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
                location = pyautogui.locateOnScreen('assets/endless/friend_competition.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击好友竞赛")
                # 点击出击
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/endless/go.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击出击")
                # 点击出击,当前在祝福界面
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/endless/go.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击出击,当前在祝福界面")
                # 监听死亡界面，等待复活按钮出现
                avoid_missile = 0
                while True:
                    try:
                        time.sleep(2)
                        revive_location = pyautogui.locateOnScreen('assets/revive.png', confidence=0.8)
                        break
                    except:
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
                ad_watch_until_end(True)

                # 第二次死亡，这次没有广告可看了，结束战斗
                avoid_missile = 0
                while True:
                    try:
                        time.sleep(2)
                        revive_40_diamond_location = pyautogui.locateOnScreen('assets/revive_40_diamond.png', confidence=0.8)
                        break
                    except:
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
                exit_battle_location = pyautogui.locateOnScreen('assets/exit_battle.png', confidence=0.8)
                pyautogui.click(exit_battle_location)
                time.sleep(5)
                logger.info("战斗结束")
                # 结算界面，可能有宝箱开
                try:
                    time.sleep(2)
                    congratulations_location = pyautogui.locateOnScreen('assets/congratulations.png', confidence=0.8)
                    get_chest_location = pyautogui.locateOnScreen('assets/get_chest.png', confidence=0.8)
                    time.sleep(2)
                    pyautogui.click(get_chest_location)
                    logger.info("结算界面，有宝箱开")
                except:
                    # 没有箱子开
                    logger.info("没有箱子开，结束了")
                    chest_full = True
                # 结算界面，点击继续,会跳转到好友竞赛和世界竞赛选择界面
                time.sleep(2)
                continue_location = pyautogui.locateOnScreen('assets/continue.png', confidence=0.8)
                pyautogui.click(continue_location)
                logger.info("点击继续，跳转到好友竞赛和世界竞赛选择界面")
            else:
                # 宝箱满了，而且世界竞赛也打完了，返回首页后关闭
                # 返回到首页
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("返回到首页")
                if close_app_after_chest_full:
                    # 点击关闭软件
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/close_app.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("点击关闭软件")
                # 循环直接结束了
                break



def shop_ad_gift():
    # 点击商店
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/shop.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击商店")
    # 点击视频广告按钮
    First_while = True
    while First_while == True:
        try:
            time.sleep(2)
            location = pyautogui.locateOnScreen('shop_ad_gift/shop_ad_video.png', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击视频广告按钮")
            # 监听广告看完情况，点击关闭界面，复活成功
            second_while = True
            ad_watch_until_end(second_while)

            time.sleep(2)
            congratulations_location = pyautogui.locateOnScreen('assets/congratulations.png', confidence=0.8)
            get_chest_location = pyautogui.locateOnScreen('assets/get_chest.png', confidence=0.8)
            time.sleep(2)
            pyautogui.click(get_chest_location)
            logger.info("奖励领取")


        except:
            logger.info("没广告可看了")
            time.sleep(5)
            location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
            time.sleep(2)
            pyautogui.click(location)
            logger.info('返回主界面')
            First_while = False


def explore():
    # 点击星际探索
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/explore.png', confidence=0.8)
    pyautogui.click(location)
    logger.info('点击星际探索')
    # 点击快速探索
    try:
        time.sleep(2)
        location = pyautogui.locateOnScreen('assets/quick_explore.png', confidence=0.8)
        pyautogui.click(location)
        logger.info('点击快速探索')
    except:
        logger.info('没有快速探索')
        time.sleep(5)
        location = pyautogui.locateOnScreen('assets/close_explore.png', confidence=0.8)
        time.sleep(2)
        pyautogui.click(location)
        logger.info('关闭探索')
        return
    # 点击视频广告按钮
    first_while = True
    while first_while:
        try:
            time.sleep(2)
            location = pyautogui.locateOnScreen('explore/explore_ad_video.png', confidence=0.8)
            pyautogui.click(location)
            logger.info("点击视频广告按钮")
            # 监听广告看完情况，点击关闭界面，复活成功
            second_while = True
            ad_watch_until_end(second_while)

            time.sleep(2)
            congratulations_location = pyautogui.locateOnScreen('assets/congratulations.png', confidence=0.8)
            get_chest_location = pyautogui.locateOnScreen('assets/get_chest.png', confidence=0.8)
            time.sleep(2)
            pyautogui.click(get_chest_location)
            logger.info("奖励领取")
        except:
            logger.info("没广告可看了")
            time.sleep(5)
            location = pyautogui.locateOnScreen('assets/close_explore.png', confidence=0.8)
            time.sleep(2)
            pyautogui.click(location)
            logger.info('关闭探索')
            first_while = False

def energy_buy(ad_video_buy_count = 4):
    # 点击能量购买页面
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/energy/energy_buy.png', confidence=0.8)
    pyautogui.click(location)
    logger.info('点击体力购买页面')
    # 开始看广告免费买体力
    while ad_video_buy_count > 0:
        try:
            time.sleep(2)
            location = pyautogui.locateOnScreen('assets/energy/energy_buy_ad_video.png', confidence=0.98)
            pyautogui.click(location)
            logger.info("点击视频广告按钮")
            ad_watch_until_end(second_while=True)
            ad_video_buy_count = ad_video_buy_count - 1
        except:
            logger.info("没广告可看了")
            first_while = False
    # 免费体力拿完了
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/energy/close_energy_buy.png', confidence=0.8)
    pyautogui.click(location)



def count_materials(image_path, template_path):
    # 读取原始图像
    img_rgb = cv2.imread(image_path)
    # 读取模板图像
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_path, 0)
    # 获取模板图像的高宽
    w, h = template.shape[::-1]
    # 进行模板匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # 设置阈值，筛选出匹配度较高的位置
    threshold = 0.8
    loc = np.where(res >= threshold)
    # 统计匹配到的模板数量
    count = len(loc[0])
    # 在原始图像上绘制匹配到的位置
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    # 显示结果图像
    cv2.imshow('Detected', img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return count



def capture_game_window_screenshot(window_title, screenshot_filename='game_screenshot.png'):
    try:
        # 查找指定标题的窗口
        game_window = gw.getWindowsWithTitle(window_title)[0]
        # 激活窗口
        game_window.activate()
        # 获取窗口的位置和大小
        left, top, width, height = game_window.left, game_window.top, game_window.width, game_window.height
        # 截取窗口区域的屏幕截图
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        # 保存截图
        screenshot.save(screenshot_filename)
        logger.info("截图已保存为 %s" % screenshot_filename)
    except IndexError:
        logger.info(f"未找到标题为 {window_title} 的窗口。")
    except Exception as e:
        logger.info(f"截图时出现错误: {e}")



pytesseract.pytesseract.tesseract_cmd = r'D:/Tesseract-OCR/tesseract.exe'
def get_material_quantity(screenshot_path, template_path):
    # 读取原始图像（游戏截图）
    img_rgb = cv2.imread(screenshot_path)
    # 读取模板图像（材料图片）
    template = cv2.imread(template_path)
    # 获取模板图像的宽度和高度
    w, h = template.shape[1::-1]
    # 进行模板匹配
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    # 设置阈值，筛选出匹配度较高的位置
    threshold = 0.7
    loc = np.where(res >= threshold)
    # 取第一个匹配结果
    pt = next(zip(*loc[::-1]), None)
    if pt is None:
        logger.info("未找到匹配的材料图片。")
        return None
    # 计算数字区域的位置
    number_x = pt[0]
    number_y = pt[1]
    number_width = 100
    number_height = 100
    logger.info(f"数字区域位置: ({number_x}, {number_y}), 宽度: {number_width}, 高度: {number_height}")

    # 绘制红色矩形框框出数字区域
    cv2.rectangle(img_rgb, (number_x, number_y), (number_x + number_width, number_y + number_height), (0, 0, 255), 2)

    # 显示带有红框的图像
    cv2.imshow('Detected Number Region', img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 提取数字区域
    number_region = img_rgb[number_y:number_y + number_height, number_x:number_x + number_width]
    # 将数字区域转换为 HSV 颜色空间
    hsv = cv2.cvtColor(number_region, cv2.COLOR_BGR2HSV)

    # 定义黄色的 HSV 范围
    lower_yellow = np.array([10, 100, 100])
    upper_yellow = np.array([25, 255, 255])

    # 创建掩码，只保留黄色部分
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # 将掩码应用到数字区域
    yellow_number_region = cv2.bitwise_and(number_region, number_region, mask=mask)

    cv2.imshow('Yellow Number Region', yellow_number_region)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 将黄色部分转换为灰度图像
    yellow_number_region_gray = cv2.cvtColor(yellow_number_region, cv2.COLOR_BGR2GRAY)

    # 对数字区域进行降噪处理，例如使用中值滤波
    yellow_number_region_gray = cv2.medianBlur(yellow_number_region_gray, 3)

    # 对数字区域进行二值化处理，提高 OCR 识别准确率
    # _, binary_number_region = cv2.threshold(yellow_number_region_gray, 127, 255, cv2.THRESH_BINARY)
    quantity = pytesseract.image_to_string(yellow_number_region_gray, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    # 去除识别结果中的非数字字符
    quantity = ''.join(filter(str.isdigit, quantity))
    return quantity


def battle_stage(mode = 'endless'):
    # 监听死亡界面，等待复活按钮出现
    wait_revive = True
    avoid_missile = 0
    while wait_revive:
        try:
            time.sleep(2)
            revive_location = pyautogui.locateOnScreen('assets/revive.png', confidence=0.8)
            break
        except:
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
                    location = pyautogui.locateOnScreen('assets/standard/key.png', confidence=0.8)
                    logger.info("胜利了")
                    wait_revive = False
                except:
                    logger.info("闯关模式暂时没有胜利")
            time.sleep(5)
    if wait_revive:
        # 点击复活按钮, 看广告
        pyautogui.click(revive_location)
        logger.info("点击复活按钮, 看广告")
        # 监听广告看完情况，点击关闭界面，复活成功
        ad_watch_until_end(True)

    # 第二次死亡，这次没有广告可看了，结束战斗
    avoid_missile = 0
    while wait_revive:
        try:
            time.sleep(2)
            revive_40_diamond_location = pyautogui.locateOnScreen('assets/revive_40_diamond.png', confidence=0.8)
            break
        except:
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
                    location = pyautogui.locateOnScreen('assets/standard/key.png', confidence=0.8)
                    logger.info("胜利了")
                    wait_revive = False
                except:
                    logger.info("闯关模式暂时没有胜利")
            time.sleep(5)
    if wait_revive:
        exit_battle_location = pyautogui.locateOnScreen('assets/exit_battle.png', confidence=0.8)
        pyautogui.click(exit_battle_location)
        time.sleep(5)
        logger.info("战斗结束")
    # 结算界面，可能有宝箱开
    try:
        time.sleep(2)
        congratulations_location = pyautogui.locateOnScreen('assets/congratulations.png', confidence=0.8)
        get_chest_location = pyautogui.locateOnScreen('assets/get_chest.png', confidence=0.8)
        time.sleep(2)
        pyautogui.click(get_chest_location)
        logger.info("结算界面，有宝箱开")
    except:
        # 没有箱子开
        logger.info("没有箱子开")
        time.sleep(2)
        if mode == 'endless':
            location = pyautogui.locateOnScreen('assets/close_app.png', confidence=0.8)
            time.sleep(2)
            pyautogui.click(location)
        time.sleep(2)

    # 结算界面，点击继续
    time.sleep(2)
    if mode != 'endless':
        try:
            location = pyautogui.locateOnScreen('assets/battle_fail.png', confidence=0.8)
            battle_victory = False
        except:
            battle_victory = True
            # 检查是否有双倍奖励按钮
            try:
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/standard/ad_double_reward.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击双倍奖励")
                ad_watch_until_end(True)
            except:
                logger.info("没有双倍奖励")
    time.sleep(2)
    continue_location = pyautogui.locateOnScreen('assets/continue.png', confidence=0.8)
    pyautogui.click(continue_location)
    # 返回战斗结果
    return battle_victory

def standard(
        main_material_order=['h', '4', '5', '3'],
        sub_h_material_dict={'h-1': 0, 'h-2': 0, 'h-3': 0, 'h-4': 0, },
        sub_4_material_dict={'4-1': 0, '4-2': 0, '4-3': 0, '4-4': 0, },
        sub_5_material_dict={'5-1': 0, '5-2': 0, '5-3': 0, '5-4': 0, },
        sub_3_material_dict={'3-1': 0, '3-2': 0, '3-3': 0, '3-4': 0, },
        close_app_after_energy_empty=True,
        ):
    # 点击闯关模式
    time.sleep(2)
    location = pyautogui.locateOnScreen('assets/standard/standard_entrance.png', confidence=0.8)
    pyautogui.click(location)
    logger.info("点击闯关模式")
    # 先完整输出一下传递参数
    logger.info(f"main_material_order：{main_material_order}")
    logger.info(f"sub_h_material_dict：{sub_h_material_dict}")
    logger.info(f"sub_4_material_dict：{sub_4_material_dict}")
    logger.info(f"sub_5_material_dict：{sub_5_material_dict}")
    logger.info(f"sub_3_material_dict：{sub_3_material_dict}")

    # 本地化存储<TODO>



    # 按照星级材料顺序开打
    for material_main in main_material_order:
        # 提示要打是多少星的材料
        logger.info("要打"+str(material_main)+"星材料")
        # 不同星级材料共用的战斗顺序，每次战斗完毕后，保持从小到大的顺序
        if material_main == 'h':
            material_no_main_str = 'h'
            # 按值升序排序
            sorted_items = sorted(sub_h_material_dict.items(), key=lambda item: item[1])
            # 切换到英雄难度
            try:
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/standard/normal_to_hero_logo.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("切换到英雄难度")
            except:
                logger.info("当前位置英雄难度，不需要切换")             
        elif material_main == '4':
            material_no_main_str = '4'
            # 按值升序排序
            sorted_items = sorted(sub_4_material_dict.items(), key=lambda item: item[1])
            # 切换到普通难度
            try:
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/standard/hero_to_normal_logo.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("切换到普通难度")
            except:
                logger.info("当前位置普通难度，不需要切换")     
        elif material_main == '5':
            material_no_main_str = '5'
            # 按值升序排序
            sorted_items = sorted(sub_5_material_dict.items(), key=lambda item: item[1])
            # 切换到普通难度
            try:
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/standard/hero_to_normal_logo.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("切换到普通难度")
            except:
                logger.info("当前位置普通难度，不需要切换") 
        elif material_main == '3':
            material_no_main_str = '3'
            # 按值升序排序
            sorted_items = sorted(sub_3_material_dict.items(), key=lambda item: item[1])
            # 切换到普通难度
            try:
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/standard/hero_to_normal_logo.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("切换到普通难度")
            except:
                logger.info("当前位置普通难度，不需要切换") 
        # 输出排序后的键值对列表，发现已经是一个list了，每个元素是一个元组
        logger.info(f"按值升序排序后的键值对列表:{sorted_items}")
        # 初始化每个关卡的count数
        fail_1_cnt, fail_2_cnt, fail_3_cnt, fail_4_cnt = 0, 0, 0, 0
        total_1_cnt, total_2_cnt, total_3_cnt, total_4_cnt = 1, 1, 1, 1
        # 子关卡循环
        for main_sub_material_num_temple in sorted_items:
            # 子关卡
            material_no_sub_str = main_sub_material_num_temple[0].split('-')[1]
            logger.info("当前星级材料为："+material_no_main_str+"星，当前子关卡为："+material_no_sub_str)
            # 下方循环用的fail_cnt和total_cnt需要重置
            fail_cnt, total_cnt =0, 1
            # 同一种材料的不同关卡的循环
            while fail_cnt < total_cnt:
                # 点击快速扫荡
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/standard/quick_sweep.png', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击快速扫荡")
                # 点击对应星级材料
                if material_no_main_str != 'h':
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/standard/material_'+material_no_main_str+'.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info('点击'+material_no_main_str+'星材料')
                # 点击对应的材料
                time.sleep(2)
                location = pyautogui.locateOnScreen('assets/standard/material_'+material_no_main_str+'_'+material_no_sub_str+'.png', confidence=0.8)
                pyautogui.click(location)
                logger.info('点击'+material_no_main_str+'_'+material_no_sub_str+'材料')
                # 点击第一个要攻打的关卡, 条件是能够扫荡
                try:
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/standard/single_stage_sweep.png', confidence=0.8)
                    logger.info("有能扫荡的")
                    location = pyautogui.locateOnScreen('assets/standard/material_'+material_no_main_str+'_'+material_no_sub_str+'_no_digital.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("点击能扫荡的那个关卡材料图标")
                    # 检查有多少关卡能匹配到
                    time.sleep(2)
                    # 获取所有匹配的进入关卡按钮位置
                    stage_go_locations = list(pyautogui.locateAllOnScreen('assets/standard/stage_go.png', confidence=0.96))
                    total_cnt = len(stage_go_locations)
                    logger.info(f"有{total_cnt}个关卡能匹配到")
                    if total_cnt - fail_cnt == 0:
                        logger.info("没有能打赢的关卡了")
                        time.sleep(2)
                        location = pyautogui.locateOnScreen('assets/standard/quit_quick_sweep_and_stage_card.png', confidence=0.8)
                        pyautogui.click(location)
                        logger.info("退出材料详情页")
                        time.sleep(2)
                        location = pyautogui.locateOnScreen('assets/standard/quit_quick_sweep_and_stage_card.png', confidence=0.8)
                        pyautogui.click(location)
                        logger.info("退出快速扫荡页")
                    else:
                        # 点击total-fail的最后一个进入关卡
                        location = stage_go_locations[total_cnt - fail_cnt - 1]
                        pyautogui.click(location)
                        logger.info("点击排除失败后的最后一个关卡")
                        if str(material_main) == 'h':
                            # 点击英雄难度的扫荡按钮
                            time.sleep(2)
                            location = pyautogui.locateOnScreen('assets/standard/stage_sweep.png', confidence=0.8)
                            pyautogui.click(location)
                            logger.info("英雄难度仅扫荡，点击英雄难度扫荡")
                            # 有的关卡是新开启的或者不满3颗星，提示无法扫荡
                            try:
                                time.sleep(2)
                                location = pyautogui.locateOnScreen('assets/standard/ensure_for_strength_not_enough.png', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("提示无法扫荡，点击确定")
                                # 关闭关卡标签页
                                time.sleep(2)
                                location = pyautogui.locateOnScreen('assets/standard/quit_quick_sweep_and_stage_card.png', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击关闭关卡标签页")
                                # 更新失败次数
                                fail_cnt = fail_cnt + 1
                                logger.info(f"失败次数{fail_cnt}")
                            except:
                                # 检查出击仍然存在，说明体力已经不够继续打了
                                try:
                                    time.sleep(5)
                                    location = pyautogui.locateOnScreen('assets/standard/go.png', confidence=0.8)
                                    logger.info("点击一次出击后，仍然存在出击按钮，应该买光体力后体力没了，没办法，只能结束了")
                                    # 关闭关卡窗口，返回闯关模式
                                    time.sleep(2)
                                    location = pyautogui.locateOnScreen('assets/standard/quit_quick_sweep_and_stage_card.png',
                                                                        confidence=0.8)
                                    pyautogui.click(location)
                                    logger.info("点击关闭关卡窗口，返回闯关模式")
                                    # 返回主界面
                                    time.sleep(2)
                                    location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
                                    pyautogui.click(location)
                                    logger.info("点击返回主界面")
                                    if close_app_after_energy_empty:
                                        # 退出游戏
                                        time.sleep(2)
                                        location = pyautogui.locateOnScreen('assets/close_app.png', confidence=0.8)
                                        pyautogui.click(location)
                                        logger.info("体力不足关闭使能开启，点击关闭游戏")
                                        return
                                    else:
                                        logger.info("体力不足关闭使能关闭，停留首页")
                                        return
                                except:
                                    logger.info("体力正常够打本关，扫荡成功")
                                # 检查是否有双倍奖励按钮
                                try:
                                    time.sleep(2)
                                    location = pyautogui.locateOnScreen('assets/standard/ad_double_reward.png', confidence=0.8)
                                    pyautogui.click(location)
                                    logger.info("点击双倍奖励")
                                    ad_watch_until_end(True)
                                except:
                                    logger.info("没有双倍奖励")
                                # 广告看完，扫荡完成
                                time.sleep(2)
                                location = pyautogui.locateOnScreen('assets/standard/sweep_done.png', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击扫荡完成")
                                # 关闭关卡标签页
                                time.sleep(2)
                                location = pyautogui.locateOnScreen('assets/standard/quit_quick_sweep_and_stage_card.png', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击关闭关卡标签页")
                        else:
                            # 点击出击
                            time.sleep(2)
                            location = pyautogui.locateOnScreen('assets/standard/go.png', confidence=0.8)
                            pyautogui.click(location)
                            logger.info("点击出击")
                            # 检查出击仍然存在，说明体力已经不够继续打了
                            try:
                                time.sleep(5)
                                location = pyautogui.locateOnScreen('assets/standard/go.png', confidence=0.8)
                                logger.info("点击一次出击后，仍然存在出击按钮，应该买光体力后体力没了，没办法，只能结束了")
                                # 关闭关卡窗口，返回闯关模式
                                time.sleep(2)
                                location = pyautogui.locateOnScreen('assets/standard/quit_quick_sweep_and_stage_card.png',
                                                                    confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击关闭关卡窗口，返回闯关模式")
                                # 返回主界面
                                time.sleep(2)
                                location = pyautogui.locateOnScreen('assets/return.png', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击返回主界面")
                                if close_app_after_energy_empty:
                                    # 退出游戏
                                    time.sleep(2)
                                    location = pyautogui.locateOnScreen('assets/close_app.png', confidence=0.8)
                                    pyautogui.click(location)
                                    logger.info("体力不足关闭使能开启，点击关闭游戏")
                                    return
                                else:
                                    logger.info("体力不足关闭使能关闭，停留首页")
                                    return
                            except:
                                logger.info("体力正常够打本关")
                            # 战力不足可能出现的警告
                            try:
                                time.sleep(2)
                                location = pyautogui.locateOnScreen('assets/standard/ensure_for_strength_not_enough.png', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击战力不足的确定")
                            except:
                                logger.info("战力足够")
                            # 开始战斗, 并得到战斗结果
                            battle_victory = battle_stage(mode='standard')
                            # 检查是否有弹出无尽小组赛和无尽争霸赛
                            special_competition_show = True
                            while special_competition_show:
                                try:
                                    time.sleep(2)
                                    location = pyautogui.locateOnScreen('assets/special/later_participate.png', confidence=0.8)
                                    logger.info("弹出了无尽比赛，现在点击稍后参加")
                                    # 点击稍后参加
                                    pyautogui.click(location)
                                except:
                                    logger.info("没有弹出无尽比赛提示")
                                    special_competition_show = False
                            # 更新失败次数
                            if battle_victory == False:
                                fail_cnt = fail_cnt + 1
                                logger.info(f"失败次数{fail_cnt}")


                            # location = pyautogui.locateOnScreen('assets/standard/stage_go.png', confidence=0.8)
                            # pyautogui.click(location)
                            # logger.info("点击进入关卡")

                except:
                    logger.info("没有能扫荡的")
                    time.sleep(2)
                    location = pyautogui.locateOnScreen('assets/standard/quit_quick_sweep_and_stage_card.png', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("退出快速扫荡")
                    break







if __name__ == '__main__':
    logger.info("Hey, welcome to the game")
    # login()
    find_chest()
    energy_buy(ad_video_buy_count=4)
    # boss()
    explore()
    shop_ad_gift()
    # ad_watch_until_end()
    # endless_mode(
    #     close_app_after_chest_full=False,
    #     endless_selection='world_challenge'
    # )
    standard(
        main_material_order=['h', '4', '5', '3'],
        sub_h_material_dict={'h-1': 4 , 'h-2': 5 , 'h-3': 3 , 'h-4': 5 , },
        sub_4_material_dict={'4-1': 54, '4-2': 59, '4-3': 52, '4-4': 50, },
        sub_5_material_dict={'5-1': 24, '5-2': 25, '5-3': 24, '5-4': 23, },
        sub_3_material_dict={'3-1': 1 , '3-2': 1 , '3-3': 1 , '3-4': 1 , },
        close_app_after_energy_empty=True
    )


    # 检测是否为普通难度或英雄难度
    # time.sleep(2)
    # location = pyautogui.locateOnScreen('assets/standard/standard_entrance.png', confidence=0.8)
    # pyautogui.click(location)
    # logger.info("点击闯关模式")
    # # 检查是否为普通难度
    # hero = True
    # try:
    #     time.sleep(2)
    #     location = pyautogui.locateOnScreen('assets/standard/hero_to_normal_logo.png', confidence=0.8)
    #     logger.info("检测到英雄难度")
    # except:
    #     logger.info("检测到普通难度")
    #     hero = False






