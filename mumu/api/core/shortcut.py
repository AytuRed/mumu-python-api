#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 19:11
# @Author : wlkjyy
# @File : shortcut.py
# @Software: PyCharm
import os.path




class Shortcut:

    def __init__(self, utils):
        self.utils = utils

    def create(self, name: str, icon: str, package: str) -> bool:
        """
            Create a desktop shortcut.
        :param name: shortcut name
        :param icon: path to the shortcut icon
        :param package: package name to auto-launch from the shortcut
        :return:
        """
        self.utils.set_operate('control')

        if not os.path.exists(icon):
            raise FileNotFoundError(f'File not found: {icon}')

        ret_code, retval = self.utils.run_command(['shortcut', 'create', '-n', name, '-i', icon, '-pkg', package])

        if ret_code != 0:
            raise RuntimeError(retval)

        return True

    def delete(self) -> bool:
        """
            Delete the desktop shortcut.
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['shortcut', 'delete'])

        if ret_code != 0:
            raise RuntimeError(retval)

        return True
