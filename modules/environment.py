# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 10:03 AM
# @Author  : ailx10
# @File    : environment.py

import os

# 收集远程设备的环境变量
def run(**args):
    print("[*] in environment module.")
    return os.environ
