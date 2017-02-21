#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
class Logger():
    def __init__(self, logname='./logger.log', loglevel=logging.DEBUG):  #logname和loglevel两个参数都设置了默认值
        self.logger = logging.getLogger()
        self.logger.setLevel(loglevel)
# 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname)
        fh.setLevel(loglevel)
# 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)
# 定义handler的输出格式
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d  - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
# 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

#主函数
if __name__ == '__main__':
    logger = Logger("product.log", logging.DEBUG).getlog()
    logger.info('info message')
    logger.error("error message")
    logger.warn("warn message")
    logger.critical("critical message")

# 2017 - 01 - 19 16:55:54, 720 - INFO - mylog - < module > - 47 - info message
# 2017 - 01 - 19 16:55:54, 720 - ERROR - mylog - < module > - 48 - error message
# 2017 - 01 - 19 16:55:54, 720 - WARNING - mylog - < module > - 49 - warn message
# 2017 - 01 - 19 16:55:54, 721 - CRITICAL - mylog - < module > - 50 - critical message
