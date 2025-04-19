import cv2
import numpy as np
import pytesseract
import pyautogui
import pygetwindow as gw
from logger import logger
from ad_watch_until_end import ad_watch_until_end_by_location

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