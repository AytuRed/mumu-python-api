#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 14:17
# @Author : wlkjyy
# @File : root.py
# @Software: PyCharm
import mumu.config as config



class Root:

    def __init__(self, utils):
        self.utils = utils

    def disable(self):
        """
            Disable emulator root permission.
        :return:
        """
        self.utils.set_operate("setting")
        ret_code, ret_val = self.utils.run_command(['-k', 'root_permission', '-val', 'false'])

        if ret_code != 0:
            raise RuntimeError(ret_val)

        return True

    def enable(self):
        """
            Enable emulator root permission.
        :return:
        """
        self.utils.set_operate("setting")
        ret_code, ret_val = self.utils.run_command(['-k', 'root_permission', '-val', 'true'])

        if ret_code != 0:
            raise RuntimeError(ret_val)

        return True
