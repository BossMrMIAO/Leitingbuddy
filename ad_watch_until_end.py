import time
import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab, Image, ImageOps, ImageFilter, ImageEnhance
from logger import logger
from pyautogui import ImageNotFoundException
import pygetwindow as gw


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
        # time.sleep(2)
        # if direct_close_counter != 0 :
        #     # 截取屏幕
        #     screenshot = pyautogui.screenshot()
        #     # 对屏幕截图进行预处理
        #     processed_screenshot = process_image(screenshot)
        #     # 使用 OpenCV 进行模板匹配
        #     result = cv2.matchTemplate(processed_screenshot, processed_reference, cv2.TM_CCOEFF_NORMED)
        #     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        #     # 匹配到的区域，然后重新匹配关闭按钮的区域，并且匹配到之后点击关闭它
        #     if max_val >= 0.8:
        #         result = cv2.matchTemplate(processed_screenshot, processed_reference_ad_close, cv2.TM_CCOEFF_NORMED)
        #         min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        #         h, w = processed_reference_ad_close.shape
        #         top_left = max_loc
        #         center = (top_left[0] + w // 2, top_left[1] + h // 2)
        #         close_ad_location = center
        #         # 点击定位到的位置
        #         logger.info(f'要点击的位置是{center}')
        #         pyautogui.click(close_ad_location)
        #         logger.info("成功检测到目标元素并尝试关闭广告")
        #         try:
        #             time.sleep(0.5)
        #             location = pyautogui.locateOnWindow('assets/ad/continue_ad.png', '雷霆战机：集结', confidence=0.8)
        #             pyautogui.click(location)
        #             logger.info("广告关闭不成功，继续看完广告")
        #         except ImageNotFoundException:
        #             logger.info("广告关闭成功，复活成功")
        #             second_while = False
        #     else:
        #         close_ad_location = None
        #         logger.info(f"未找到目标元素，剩余强制点击关闭的倒计数：{direct_close_counter}")
        #         direct_close_counter = direct_close_counter - 1
        #         time.sleep(5)

        # else:
        #     # 超时的操作，看来没有定位到已看完广告，改为直接定位关闭按钮，然后直接关闭，直接点击关闭尝试
        #     logger.info('本次是检查关闭按钮，并点击关闭')
        #     result = cv2.matchTemplate(processed_screenshot, processed_reference_ad_close, cv2.TM_CCOEFF_NORMED)
        #     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        #     h, w = processed_reference_ad_close.shape
        #     top_left = max_loc
        #     center = (top_left[0] + w // 2, top_left[1] + h // 2)
        #     close_ad_location = center
        #     # 点击定位到的位置
        #     logger.info(f'要点击的位置是{center}')
        #     pyautogui.click(close_ad_location)
        #     logger.info("成功检测到目标元素并尝试关闭广告，强制点击时广告应该早就看完了")
        #     try:
        #         time.sleep(0.5)
        #         location = pyautogui.locateOnWindow('assets/ad/continue_ad.png', '雷霆战机：集结', confidence=0.8)
        #         pyautogui.click(location)
        #         logger.info("广告关闭不成功，继续看完广告")
        #     except ImageNotFoundException:
        #         logger.info("广告关闭成功与否也不知道，我就当他成功了，继续往下走了")
        #         second_while = False


        
        time.sleep(2)
        if direct_close_counter!= 0 :
            try:
                # 检查是否有关闭按钮
                time.sleep(2)
                ad_end_location = pyautogui.locateOnWindow('assets/ad/ad_end.png', '雷霆战机：集结', confidence=0.8)
                # 点击关闭广告
                close_ad_location = pyautogui.locateOnWindow('assets/ad/close_ad.png', '雷霆战机：集结', confidence=0.5)
                pyautogui.click(close_ad_location)
                logger.info("成功检测到目标元素并尝试关闭广告")
                try:
                    time.sleep(0.5)
                    location = pyautogui.locateOnWindow('assets/ad/continue_ad.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("广告关闭不成功，继续看完广告")
                except ImageNotFoundException:
                    logger.info("广告关闭成功，复活成功")
                    second_while = False
            except ImageNotFoundException:
                logger.info(f"未找到目标元素，剩余强制点击关闭的倒计数：{direct_close_counter}")
                direct_close_counter = direct_close_counter - 1
                time.sleep(5)
        else:
            # 超时的操作，看来没有定位到已看完广告，改为直接定位关闭按钮，然后直接关闭，直接点击关闭尝试
            logger.info('本次是检查关闭按钮，并点击关闭')
            # 检查是否有关闭按钮
            time.sleep(2)
            # 点击关闭广告
            close_ad_location = pyautogui.locateOnWindow('assets/ad/close_ad.png', '雷霆战机：集结', confidence=0.5)
            pyautogui.click(close_ad_location)
            second_while = False

def get_window_dimensions(window_title):
    try:
        # 根据窗口标题查找窗口
        window = gw.getWindowsWithTitle(window_title)[0]
        # 确保窗口是可见的
        if window.visible:
            # 获取窗口的四维信息
            x = window.left
            y = window.top
            width = window.width
            height = window.height
            return x, y, width, height
        else:
            print("窗口不可见。")
    except IndexError:
        print(f"未找到标题为 '{window_title}' 的窗口。")
    return None

def ad_watch_until_end_by_location(direct_close_counter = 7):
    # 获取游戏窗口坐标
    x,y,width,height = get_window_dimensions('雷霆战机：集结')
    # 等待30秒走过后直接点击关闭按钮
    while direct_close_counter != 0:
        time.sleep(5)
        logger.info(f"剩余强制点击关闭的倒计数：{direct_close_counter}")
        direct_close_counter = direct_close_counter - 1
    # 关闭按钮相对位置偏移
    offset_x,offset_y = 700,140
    # 直接点击关闭按钮
    pyautogui.click(x+offset_x,y+offset_y)
    logger.info("设定时间到达，根据位置关闭广告")


# try:
#     while True:
#         print(get_window_dimensions('雷霆战机：集结'))
#         x, y = pyautogui.position()
#         print(f"当前鼠标坐标: X = {x}, Y = {y}")
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("\n程序已停止。")    
# 
# ad_watch_until_end_by_location(direct_close_counter=8)    

