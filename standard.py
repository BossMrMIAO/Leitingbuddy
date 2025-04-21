import time
import pyautogui
from pyautogui import ImageNotFoundException
from logger import logger
from ad_watch_until_end import get_window_dimensions,ad_watch_until_end_by_location
from battle_stage import battle_stage




def standard(
        main_material_order=['h', '4', '5', '3'],
        stage_offset_list=['0', '0', '0', '0'],
        sub_h_material_dict={'h-1': 0, 'h-2': 0, 'h-3': 0, 'h-4': 0, },
        sub_4_material_dict={'4-1': 0, '4-2': 0, '4-3': 0, '4-4': 0, },
        sub_5_material_dict={'5-1': 0, '5-2': 0, '5-3': 0, '5-4': 0, },
        sub_3_material_dict={'3-1': 0, '3-2': 0, '3-3': 0, '3-4': 0, },
        close_app_after_energy_empty=True,
        normal_confidence=0.96, hero_confidence=0.96,
        ):
    # 获取游戏窗口坐标
    x,y,width,height = get_window_dimensions('雷霆战机：集结')
    # 点击闯关模式
    time.sleep(2)
    location = pyautogui.locateOnWindow('assets/standard/standard_entrance.png', '雷霆战机：集结', confidence=0.8)
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
    for index,material_main in enumerate(main_material_order):
        # 提示要打是多少星的材料
        logger.info("要打"+str(material_main)+"星材料")
        # 读取对应的偏移量
        stage_offset = stage_offset_list[index]
        # 不同星级材料共用的战斗顺序，每次战斗完毕后，保持从小到大的顺序
        if material_main == 'h':
            material_no_main_str = 'h'
            # 按值升序排序
            sorted_items = sorted(sub_h_material_dict.items(), key=lambda item: item[1])
            # 切换到英雄难度
            try:
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/standard/normal_to_hero_logo.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("切换到英雄难度")
            except ImageNotFoundException:
                logger.info("当前位置英雄难度，不需要切换")             
        elif material_main == '4':
            material_no_main_str = '4'
            # 按值升序排序
            sorted_items = sorted(sub_4_material_dict.items(), key=lambda item: item[1])
            # 切换到普通难度
            try:
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/standard/hero_to_normal_logo.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("切换到普通难度")
            except ImageNotFoundException:
                logger.info("当前位置普通难度，不需要切换")     
        elif material_main == '5':
            material_no_main_str = '5'
            # 按值升序排序
            sorted_items = sorted(sub_5_material_dict.items(), key=lambda item: item[1])
            # 切换到普通难度
            try:
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/standard/hero_to_normal_logo.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("切换到普通难度")
            except ImageNotFoundException:
                logger.info("当前位置普通难度，不需要切换") 
        elif material_main == '3':
            material_no_main_str = '3'
            # 按值升序排序
            sorted_items = sorted(sub_3_material_dict.items(), key=lambda item: item[1])
            # 切换到普通难度
            try:
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/standard/hero_to_normal_logo.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("切换到普通难度")
            except ImageNotFoundException:
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
            fail_cnt, total_cnt = 0, 1+stage_offset
            # 同一种材料的不同关卡的循环
            while fail_cnt < total_cnt - stage_offset:
                # 点击快速扫荡
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/standard/quick_sweep.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info("点击快速扫荡")
                # 点击对应星级材料
                if material_no_main_str != 'h':
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/standard/material_'+material_no_main_str+'.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info('点击'+material_no_main_str+'星材料')
                # 点击对应的材料
                time.sleep(2)
                location = pyautogui.locateOnWindow('assets/standard/material_'+material_no_main_str+'_'+material_no_sub_str+'.png', '雷霆战机：集结', confidence=0.8)
                pyautogui.click(location)
                logger.info('点击'+material_no_main_str+'_'+material_no_sub_str+'材料')
                # 点击第一个要攻打的关卡, 条件是能够扫荡
                try:
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/standard/single_stage_sweep.png', '雷霆战机：集结', confidence=0.8)
                    logger.info("有能扫荡的")
                    location = pyautogui.locateOnWindow('assets/standard/material_'+material_no_main_str+'_'+material_no_sub_str+'_no_digital.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("点击能扫荡的那个关卡材料图标")
                    # 检查有多少关卡能匹配到
                    time.sleep(2)
                    # 获取所有匹配的进入关卡按钮位置
                    if material_main == 'h':
                        stage_go_locations = list(pyautogui.locateAllOnScreen('assets/standard/stage_go_hero.png', 
                                region=(x+180,y+850,660-180,1040-850), confidence=hero_confidence))
                        stage_lock_location = list(pyautogui.locateAllOnScreen('assets/standard/hero_lock_stage.png', 
                                region=(x+180,y+850,660-180,1040-850), grayscale=True, confidence=0.8))
                    else:
                        stage_go_locations = list(pyautogui.locateAllOnScreen('assets/standard/stage_go.png', 
                                region=(x+180,y+850,660-180,1040-850), confidence=normal_confidence))
                        stage_lock_location = list(pyautogui.locateAllOnScreen('assets/standard/normal_lock_stage.png', 
                                region=(x+180,y+850,660-180,1040-850), grayscale=True, confidence=0.8))
                    print(f'{len(stage_go_locations)}个关卡能匹配到，{len(stage_lock_location)}个关卡锁定')
                    total_cnt = len(stage_go_locations)
                    # 排除活动关卡
                    # try:
                    #     time.sleep(2)
                    #     location = pyautogui.locateOnWindow('assets/standard/special_missile_battlefield_available.png', '雷霆战机：集结', confidence=0.8)
                    #     logger.info("有活动关卡, 从total_cnt中减去一个活动关卡")
                    #     total_cnt = total_cnt - 1
                    # except ImageNotFoundException:
                    #     logger.info("没有活动关卡，或者活动关卡打不了")
                    logger.info(f"有{total_cnt}个关卡能匹配到，关卡偏移{stage_offset}, fail的关卡{fail_cnt}个")
                    stage_go_locations = stage_go_locations[stage_offset:]
                    logger.info(f"当前可攻打的关卡有{len(stage_go_locations)-fail_cnt}个")
                    if total_cnt - stage_offset - fail_cnt <= 0:
                        logger.info("没有能打赢的关卡了")
                        time.sleep(2)
                        location = pyautogui.locateOnWindow('assets/standard/quit_quick_sweep_and_stage_card.png', '雷霆战机：集结', confidence=0.8)
                        pyautogui.click(location)
                        logger.info("退出材料详情页")
                        time.sleep(2)
                        location = pyautogui.locateOnWindow('assets/standard/quit_quick_sweep_and_stage_card.png', '雷霆战机：集结', confidence=0.8)
                        pyautogui.click(location)
                        logger.info("退出快速扫荡页")
                    else:
                        # 点击total-fail的最后一个进入关卡
                        location = stage_go_locations[total_cnt - stage_offset - fail_cnt - 1]
                        pyautogui.click(location)
                        logger.info("点击排除失败后的最后一个关卡")
                        if str(material_main) == 'h':
                            # 点击英雄难度的扫荡按钮
                            time.sleep(2)
                            location = pyautogui.locateOnWindow('assets/standard/stage_sweep.png', '雷霆战机：集结', confidence=0.8)
                            pyautogui.click(location)
                            logger.info("英雄难度仅扫荡，点击英雄难度扫荡")
                            # 有的关卡是新开启的或者不满3颗星，提示无法扫荡
                            try:
                                time.sleep(2)
                                location = pyautogui.locateOnWindow('assets/standard/ensure_for_strength_not_enough.png', '雷霆战机：集结', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("提示无法扫荡，点击确定")
                                # 关闭关卡标签页
                                time.sleep(2)
                                location = pyautogui.locateOnWindow('assets/standard/quit_quick_sweep_and_stage_card.png', '雷霆战机：集结', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击关闭关卡标签页")
                                # 更新失败次数
                                fail_cnt = fail_cnt + 1
                                logger.info(f"失败次数{fail_cnt}")
                            except ImageNotFoundException:
                                # 检查出击仍然存在，说明体力已经不够继续打了
                                try:
                                    time.sleep(5)
                                    location = pyautogui.locateOnWindow('assets/standard/go.png', '雷霆战机：集结', confidence=0.9)
                                    logger.info("点击一次出击后，仍然存在出击按钮，应该买光体力后体力没了，没办法，只能结束了")
                                    # 关闭关卡窗口，返回闯关模式
                                    time.sleep(2)
                                    location = pyautogui.locateOnWindow('assets/standard/quit_quick_sweep_and_stage_card.png',
                                                                        '雷霆战机：集结', confidence=0.8)
                                    pyautogui.click(location)
                                    logger.info("点击关闭关卡窗口，返回闯关模式")
                                    # 返回主界面
                                    time.sleep(2)
                                    location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
                                    pyautogui.click(location)
                                    logger.info("点击返回主界面")
                                    if close_app_after_energy_empty:
                                        # 退出游戏
                                        time.sleep(2)
                                        location = pyautogui.locateOnWindow('assets/close_app.png', '雷霆战机：集结', confidence=0.8)
                                        pyautogui.click(location)
                                        logger.info("体力不足关闭使能开启，点击关闭游戏")
                                        return
                                    else:
                                        logger.info("体力不足关闭使能关闭，停留首页")
                                        return
                                except ImageNotFoundException:
                                    logger.info("体力正常够打本关，扫荡成功")
                                # 检查是否有双倍奖励按钮
                                try:
                                    time.sleep(2)
                                    location = pyautogui.locateOnWindow('assets/standard/ad_double_reward.png', '雷霆战机：集结', confidence=0.8)
                                    pyautogui.click(location)
                                    logger.info("点击双倍奖励")
                                    ad_watch_until_end_by_location()
                                except ImageNotFoundException:
                                    logger.info("没有双倍奖励")
                                # 广告看完，扫荡完成
                                time.sleep(2)
                                location = pyautogui.locateOnWindow('assets/standard/sweep_done.png', '雷霆战机：集结', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击扫荡完成")
                                # 关闭关卡标签页
                                time.sleep(2)
                                location = pyautogui.locateOnWindow('assets/standard/quit_quick_sweep_and_stage_card.png', '雷霆战机：集结', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击关闭关卡标签页")
                        else:
                            # 点击出击
                            time.sleep(2)
                            location = pyautogui.locateOnWindow('assets/standard/go.png', '雷霆战机：集结', confidence=0.8)
                            pyautogui.click(location)
                            logger.info("点击出击")
                            # 检查出击仍然存在
                            # 体力，战力（0，0）：优先弹出没有3秒左右的没有体力弹窗，然后出击按钮还在，action: 关闭窗口，返回首页，关闭app
                            # 体力，战力（0，1）：弹出没有体力弹窗，然后出击按钮还在，关闭窗口，返回首页
                            # 体力，战力（1，0）：弹出战力不足提示，也就是确定键，出击按钮不在，直接点击确定，关闭窗口，返回首页
                            # 体力，战力（1，1）：直接出击正常完成
                            # 综合一下，点击出击后，先检查是否有战力不足按钮，如果有，说明体力充足，可以打，点击确定
                            #  如果没有战力不足的按钮情况下，再次检查有没有
                            try:
                                # 检查是否战力不足提示
                                time.sleep(2)
                                location = pyautogui.locateOnWindow('assets/standard/ensure_for_strength_not_enough.png', '雷霆战机：集结', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击战力不足的确定")
                            except ImageNotFoundException:
                                logger.info("战力正常够打本关")
                            try:
                                time.sleep(5)
                                location = pyautogui.locateOnWindow('assets/standard/go.png', '雷霆战机：集结', confidence=0.9)
                                logger.info("点击一次出击后，仍然存在出击按钮，应该买光体力后体力没了，没办法，只能结束了")
                                # 关闭关卡窗口，返回闯关模式
                                time.sleep(2)
                                location = pyautogui.locateOnWindow('assets/standard/quit_quick_sweep_and_stage_card.png',
                                                                    '雷霆战机：集结', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击关闭关卡窗口，返回闯关模式")
                                # 返回主界面
                                time.sleep(2)
                                location = pyautogui.locateOnWindow('assets/return.png', '雷霆战机：集结', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击返回主界面")
                                if close_app_after_energy_empty:
                                    # 退出游戏
                                    time.sleep(2)
                                    location = pyautogui.locateOnWindow('assets/close_app.png', '雷霆战机：集结', confidence=0.8)
                                    pyautogui.click(location)
                                    logger.info("体力不足关闭使能开启，点击关闭游戏")
                                    return
                                else:
                                    logger.info("体力不足关闭使能关闭，停留首页")
                                    return
                            except ImageNotFoundException:
                                logger.info("体力正常够打本关")
                            # 战力不足可能出现的警告
                            try:
                                time.sleep(2)
                                location = pyautogui.locateOnWindow('assets/standard/ensure_for_strength_not_enough.png', '雷霆战机：集结', confidence=0.8)
                                pyautogui.click(location)
                                logger.info("点击战力不足的确定")
                            except ImageNotFoundException:
                                logger.info("战力足够")
                            # 开始战斗, 并得到战斗结果
                            battle_victory = battle_stage(mode='standard')
                            # 检查是否有弹出无尽小组赛和无尽争霸赛
                            special_competition_show = True
                            while special_competition_show:
                                try:
                                    time.sleep(2)
                                    location = pyautogui.locateOnWindow('assets/special/later_participate.png', '雷霆战机：集结', confidence=0.8)
                                    logger.info("弹出了无尽比赛，现在点击稍后参加")
                                    # 点击稍后参加
                                    pyautogui.click(location)
                                except ImageNotFoundException:
                                    logger.info("没有弹出无尽比赛提示")
                                    special_competition_show = False
                            # 更新失败次数
                            if battle_victory == False:
                                fail_cnt = fail_cnt + 1
                                logger.info(f"失败次数{fail_cnt}")


                            # location = pyautogui.locateOnWindow('assets/standard/stage_go.png', '雷霆战机：集结', confidence=0.8)
                            # pyautogui.click(location)
                            # logger.info("点击进入关卡")

                except ImageNotFoundException:
                    logger.info("没有能扫荡的")
                    time.sleep(2)
                    location = pyautogui.locateOnWindow('assets/standard/quit_quick_sweep_and_stage_card.png', '雷霆战机：集结', confidence=0.8)
                    pyautogui.click(location)
                    logger.info("退出快速扫荡")
                    break

