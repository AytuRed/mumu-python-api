#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 15:26
# @Author : wlkjyy
# @File : app.py
# @Software: PyCharm
import json
import os.path




class App:

    def __init__(self, utils):
        self.utils = utils

    def install(self, apk_path: str = None) -> bool:
        """
            Install an app into the emulator.
        :param apk_path: path to the apk file (supports .apk/.xapk/.apks)
        :return:
        """
        if not os.path.exists(apk_path):
            raise FileNotFoundError(f"apk_path:{apk_path} not found")

        if not os.path.isfile(apk_path):
            raise FileNotFoundError(f"apk_path:{apk_path} is not a file")
        self.utils.set_operate('control')

        ret_code, retval = self.utils.run_command(['app', 'install', '-apk', apk_path])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def uninstall(self,package: str) -> bool:
        """
            Uninstall an app.
        :param package: package name to uninstall
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['app', 'uninstall', '-pkg', package])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def launch(self,package: str) -> bool:
        """
            Launch an app.
        :param package: package name to launch
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['app', 'launch', '-pkg', package])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def close(self,package: str) -> bool:
        """
            Close an app.
        :param package: package name to close
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['app', 'close', '-pkg', package])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def get_installed(self):
        """
            Get installed apps.
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['app', 'info','-i'])

        if ret_code != 0:
            raise RuntimeError(retval)

        data = json.loads(retval)
        installed = []

        for key in data.keys():
            if key != "active":
                installed.append({
                    "package": key,
                    "app_name": data[key]['app_name'],
                    "version": data[key]['version']
                })

        return installed


    def exists(self,package: str) -> bool:
        """
            Check whether an app is installed.
        :param package: package name to check
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['app', 'info', '-pkg', package])

        if ret_code != 0:
            raise RuntimeError(retval)

        data = json.loads(retval)

        return data['state'] != 'not_installed'

    def doesntExists(self,package: str) -> bool:
        """
            Check whether an app is NOT installed.
        :param package: package name to check
        :return:
        """
        return not self.exists(package)

    def state(self,package: str) -> str:
        """
            Get the app state.
        :param package: package name to query
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['app', 'info', '-pkg', package])

        if ret_code != 0:
            raise RuntimeError(retval)

        data = json.loads(retval)

        return data['state']