#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/30 08:40
# @Author : wlkjyy
# @File : Adb.py
# @Software: PyCharm
import json
import os.path
import warnings
from typing import Union


import mumu.config as config


class Adb:

    def __init__(self, utils):
        self.utils = utils

    def __run_adb_cmd(self, cmd: str):
        self.utils.set_operate('adb')
        ret_code, retval = self.utils.run_command(['-c', cmd])

        if ret_code == 0:
            return True

        raise RuntimeError(retval or f"adb command failed: {cmd}")

    def get_connect_info(self):
        """
        Get ADB connection info.
        :return: dict of ADB connection info, or (None, None) if unavailable.
        """
        self.utils.set_operate("adb")
        ret_code, retval = self.utils.run_command([''])

        if ret_code != 0:
            return None, None

        try:
            data = json.loads(retval)
        except json.JSONDecodeError:
            return None, None

        adb_info = {}
        for key, value in data.items():
            if key == "adb_host" and "adb_port" in data:
                return data["adb_host"], data["adb_port"]

            if not isinstance(value, dict):
                continue

            if 'errcode' in value:
                adb_info[key] = (None, None)
            else:
                adb_info[key] = (value.get("adb_host"), value.get("adb_port"))

        return adb_info if adb_info else (None, None)

    def click(self, x: int, y: int):
        """
            Tap (click).
        :param x: x coordinate
        :param y: y coordinate
        :return:
        """
        return self.__run_adb_cmd(f"shell input tap {x} {y}")

    def swipe(self, from_x: int, from_y: int, to_x: int, to_y: int, duration: int = 500):
        """
            Swipe.
        :param from_x: start x coordinate
        :param from_y: start y coordinate
        :param to_x: end x coordinate
        :param to_y: end y coordinate
        :param duration: swipe duration in ms
        :return:
        """
        return self.__run_adb_cmd(f"shell input swipe {from_x} {from_y} {to_x} {to_y} {duration}")

    def input_text(self, text: str):
        """
            Input text.
        :param text: text to input
        :return:
        """
        return self.__run_adb_cmd(f"input_text {text}")

    def key_event(self, key: Union[int, str]):
        """
            Key event.
        :param key: key code
        :return:
        """
        return self.__run_adb_cmd(f"shell input keyevent {key}")

    def __connect(self):
        """
            Get an available connection.
        :return:
        """

        self.utils.set_operate("adb")
        ret_code, retval = self.utils.run_command([''])

        if ret_code != 0:
            return

        try:
            data = json.loads(retval)
        except json.JSONDecodeError:
            return

        for key, value in data.items():
            if key == "adb_host" and "adb_port" in data:
                yield data["adb_host"], data["adb_port"]
                return

            if not isinstance(value, dict):
                continue

            if 'errcode' in value:
                continue
            else:
                yield value.get("adb_host"), value.get("adb_port")

    def push(self, src: str, path: str):
        """
            Transfer a file (push).
        :param src: source file
        :param path: destination path
        :return:
        """

        if not os.path.exists(src):
            raise FileNotFoundError(f"File not found: {src}")

        adb_path = self.utils.get_adb_path() or config.ADB_PATH
        if not os.path.exists(adb_path):
            raise FileNotFoundError(f"adb not found in {adb_path}")

        connect_list = list(self.__connect() or [])
        if not connect_list:
            raise RuntimeError("No available adb connections found")

        for (host, port) in connect_list:
            ret_code, retval = self.utils.run_command([adb_path, '-s', f"{host}:{port}", 'push', src, path],
                                                      mumu=False)

            if ret_code != 0:
                warnings.warn(retval)

        return True

    def push_download(self, src: str, new_name: str = None):
        """
            Transfer a file into the Download folder (push).
        :param new_name:
        :param src: source file
        :return:
        """
        if new_name:
            filename = new_name
        else:
            filename = os.path.basename(src)

        return self.push(src, f"/sdcard/Download/{filename}")

    def pull(self, src: str, path: str):
        """
            Transfer a file (pull).
        :param src: source file
        :param path: destination path
        :return:
        """

        adb_path = self.utils.get_adb_path() or config.ADB_PATH
        if not os.path.exists(adb_path):
            raise FileNotFoundError(f"adb not found in {adb_path}")

        connect_list = list(self.__connect() or [])
        if not connect_list:
            raise RuntimeError("No available adb connections found")

        for (host, port) in connect_list:
            ret_code, retval = self.utils.run_command([adb_path, '-s', f"{host}:{port}", 'pull', src, path],
                                                      mumu=False)

            if ret_code != 0:
                warnings.warn(retval)

        return True

    def clear(self, package: str):
        """
            Clear app data.
        :param package: package name
        :return:
        """
        return self.__run_adb_cmd(f"shell pm clear {package}")
