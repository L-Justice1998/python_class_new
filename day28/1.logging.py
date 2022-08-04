# Creator:justice 廖振谊
# Creat time:2022/6/30 17:48

import logging

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

log_file='log.txt'
file_handler=logging.FileHandler(log_file,mode='a')
file_handler.setLevel(logging.DEBUG)

current_handler=logging.StreamHandler()
current_handler.setLevel(logging.WARNING)

output_context=logging.Formatter("%(asctime)s -%(filename)s[line:%(lineno)d] -%(levelname)s:%(message)s"
                                 " process_num: %(process)d")
file_handler.setFormatter(output_context)
current_handler.setFormatter(output_context)

logger.addHandler(file_handler)
logger.addHandler(current_handler)

logger.debug('这是 logger debug message')
logger.info('这是 logger info message')
logger.warning('这是 logger warning message')
logger.error('这是 logger error message')
logger.critical('这是 logger critical message')

