#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/10/25 21:14
# @Author   :day day up up
# @File     :read_config.py
import configparser
class ReadConfig:
    def read_config(self, file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8")
        return cf.get(section, option)
if __name__ == '__main__':
    res = ReadConfig().read_config("case.config", "MODE", "mode")
    print(res)
