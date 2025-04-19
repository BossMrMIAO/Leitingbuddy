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