# -*- coding: utf-8 -*-
# @Time    : 2023/10/8 16:00
# @Author  : 0x000x00
# @File    : main.py
# @Software: PyCharm
# @Description: 主程序入口

# User defined modules
from logger import logger
from login import login
from find_chest import find_chest
# from boss import boss
from endless_mode import endless_mode
from energy_buy import energy_buy
from explore import explore
from shop_ad_gift import shop_ad_gift
from standard import standard



if __name__ == '__main__':
    logger.info("Hey, welcome to the game")
    # login()
    
    # endless_mode(
    #     close_app_after_chest_full=False,
    #     buddy_help_enable_flag=True,
    #     endless_selection='world_challenge'
    # )
    # find_chest()
    # explore()
    # shop_ad_gift()
    # energy_buy(ad_video_buy_count=2)
    standard(
        main_material_order=['4','5','3','h',],
        stage_offset_list=[2, 0, 0, 0, ],
        sub_h_material_dict={'h-1': 0 , 'h-2': 0, 'h-3': 1, 'h-4': 1 , },
        sub_4_material_dict={'4-1': 36, '4-2': 38, '4-3': 33, '4-4': 27, },
        sub_5_material_dict={'5-1': 11, '5-2': 11, '5-3': 11, '5-4': 11, },
        sub_3_material_dict={'3-1': 1 , '3-2': 1 , '3-3': 1 , '3-4': 1 , },
        close_app_after_energy_empty=True,
        normal_confidence=0.968, hero_confidence=0.975
    )

    # from pywinauto import Application
    # # from pywinauto import Application
    # import win32api
    # import win32con
    # import win32gui

    # def background_click(window, x, y, relative_to="client"):
    #     """
    #     在指定窗口的后台位置发送点击事件
    #     :param window: pywinauto窗口对象
    #     :param x: 横坐标
    #     :param y: 纵坐标
    #     :param relative_to: 坐标系基准，"client"（窗口客户区）或 "screen"（屏幕绝对坐标）
    #     """
    #     hwnd = window.handle
    #     if relative_to == "screen":
    #         # 将屏幕坐标转换为窗口客户区坐标
    #         client_x, client_y = win32gui.ScreenToClient(hwnd, (x, y))
    #     elif relative_to == "client":
    #         client_x, client_y = x, y
    #     else:
    #         raise ValueError("relative_to 参数应为 'client' 或 'screen'")

    #     # 组合坐标值（Windows API要求）
    #     lparam = win32api.MAKELONG(client_x, client_y)
        
    #     # 发送鼠标按下和释放消息
    #     win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lparam)
    #     win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, lparam)

    # app = Application().connect(title="雷霆战机：集结")
    # window = app.window(title="雷霆战机：集结")

    # # 直接操作控件（通过后台消息）
    # edit_control = window.Edit
    # # edit_control.set_focus()  # 非必要，后台输入可不激活窗口

    # # 拿到窗口的客户区坐标或绝对坐标
    # time.sleep(2)
    # location = pyautogui.locateOnWindow('assets/shop.png', '雷霆战机：集结', confidence=0.8)
    # print(location)
    # logger.info("点击商店")


    # time.sleep(2)
    # background_click(window, x=2080+22, y=500+22, relative_to="screen")  # 点击输入框
    # print("后台点击完成")




   





