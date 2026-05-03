#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 14:59
# @Author : wlkjyy
# @File : bridge.py
# @Software: PyCharm



class Bridge:
    def __init__(self, utils):
        self.utils = utils

    """
        Network bridge driver.
    """

    def install(self):
        """
            Install the NIC bridge driver.
        :return:
        """
        self.utils.set_operate(['driver', 'install'])
        ret_code, ret_val = self.utils.run_command(['-n', 'lwf'])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)

    def uninstall(self):
        """
            Uninstall the NIC bridge driver.
        :return:
        """
        self.utils.set_operate(['driver', 'uninstall'])
        ret_code, ret_val = self.utils.run_command([])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)
