#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/11/4 15:14
# @Author   :day day up up
# @File     :my_log.py
import logging
class MyLog:
    def my_log(self,level,msg):
        # 定义一个日志收集器 my_logger
        my_logger = logging.getLogger("log日志收集器")
        # 设定级别
        my_logger.setLevel("DEBUG")
        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        # 创建一个我们自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)
        fh = logging.FileHandler("python11.txt", encoding="utf-8")
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)
        # 两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        # 收集日志
        if level == "DEBUG":
            my_logger.info(msg)
        elif level == "INFO":
            my_logger.info(msg)
        elif level == "WARNING":
            my_logger.warning(msg)
        elif level == "ERROR":
            my_logger.error(msg)
        elif level == "CRITICAL":
            my_logger.critical(msg)
        #关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)
    def debug(self,msg):
        self.my_log("DEBUG",msg)
    def info(self,msg):
        self.my_log("INFO",msg)
    def warning(self,msg):
        self.my_log("WARNING",msg)
    def error(self,msg):
        self.my_log("ERROR",msg)
    def critical(self,msg):
        self.my_log("CRITICAL",msg)
if __name__ == '__main__':
    pass
    # my_logger = MyLog()
    # my_logger.error("笨笨")
    # my_logger.info("琪琪")