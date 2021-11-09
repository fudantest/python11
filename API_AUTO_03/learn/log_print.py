#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/11/4 14:39
# @Author   :day day up up
# @File     :log_print.py
import logging
#定义一个日志收集器 my_logger
my_logger = logging.getLogger("log日志收集器")
#设定级别
my_logger.setLevel("DEBUG")
#设置输出格式
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
#创建一个我们自己的输出渠道
ch = logging.StreamHandler()
ch.setLevel("DEBUG")
ch.setFormatter(formatter)
fh = logging.FileHandler("python11.txt",encoding="utf-8")
fh.setLevel("DEBUG")
fh.setFormatter(formatter)
#两者对接
my_logger.addHandler(ch)
my_logger.addHandler(fh)
#收集日志
my_logger.debug("log日志打印-debug")
my_logger.error("log日志打印-error")
