#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :2021/11/3 20:52
# @Author   :day day up up
# @File     :read_config.py
import configparser
from tools import project_path

class ReadConfig:
    @staticmethod
    def get_config(file_path,section,option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]
if __name__ == '__main__':
    print(ReadConfig.get_config(project_path.case_config_path,'MODE','mode'))
    print(type(ReadConfig.get_config(project_path.case_config_path, 'MODE', 'mode')))
    print(eval(ReadConfig.get_config(project_path.case_config_path, 'MODE', 'mode')))
    mode = eval(ReadConfig.get_config(project_path.case_config_path, 'MODE', 'mode'))
    for key in mode:
        if mode[key] == "all":
            pass
        else:
            for case_id in mode[key]:
                print(case_id,end="、")