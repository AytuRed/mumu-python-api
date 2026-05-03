#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 20:20
# @Author : wlkjyy
# @File : setting.py
# @Software: PyCharm
import json
import os.path
from typing import Union


class Setting:

    def __init__(self, utils):
        self.utils = utils

    def all(self, all_writable: bool = False) -> dict:
        """
            Get all settings.
        :return:
        """
        self.utils.set_operate("setting")
        if all_writable:
            args = ["-aw"]
        else:
            args = ["-a"]

        ret_code, retval = self.utils.run_command(args)
        if ret_code == 0:
            return json.loads(retval)

        raise RuntimeError(retval)

    def get(self, *args) -> Union[dict, str]:
        """
            Get one or more settings.
        :param args:
        :return:
        """
        self.utils.set_operate("setting")
        command_args = []
        for arg in args:
            command_args.extend(["-k", arg])

        ret_code, retval = self.utils.run_command(command_args)
        if ret_code == 0:
            ret = json.loads(retval)
            for key in ret.keys():
                # Type coercion
                val = ret[key]
                if isinstance(val, str) and val.isdigit():
                    ret[key] = int(val)
                elif isinstance(val, str) and val.lower() == "true":
                    ret[key] = True
                elif isinstance(val, str) and val.lower() == "false":
                    ret[key] = False

            # return ret
            if len(args) == 1:
                return ret[args[0]]

            return ret

        raise RuntimeError(retval)

    def set(self, **kwargs) -> bool:
        """
            Set one or more settings.
        :param kwargs:
        :return:
        """
        self.utils.set_operate("setting")
        command_args = []
        for key in kwargs.keys():

            if isinstance(kwargs[key], bool):
                kwargs[key] = str(kwargs[key]).lower()

            if kwargs[key] is None:
                kwargs[key] = "__null__"

            new_key = key
            if '___' in new_key:
                new_key = new_key.replace('___', '-')

            if '__' in new_key:
                new_key = new_key.replace('__', '.')

            command_args.extend(["-k", new_key, "-val", str(kwargs[key])])

        ret_code, retval = self.utils.run_command(command_args)
        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def set_by_json(self, file_path: str) -> bool:
        """
            Apply settings from a JSON file.
        :param file_path: path to the JSON file
        :return:
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)

        self.utils.set_operate("setting")
        ret_code, retval = self.utils.run_command(["-p", file_path])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def equal(self, key: str, value) -> bool:
        """
            Check whether a setting equals a value.
        :param key: setting key
        :param value: value to compare
        :return:
        """
        return self.get(key) == value

    def not_equal(self, key: str, value) -> bool:
        """
            Check whether a setting does NOT equal a value.
        :param key: setting key
        :param value: value to compare
        :return:
        """
        return self.get(key) != value

    def equal_then_set(self, key: str, value, new_value) -> bool:
        """
            If a setting equals a value, set it to a new value.
        :param key: setting key
        :param value: value to compare
        :param new_value: new value to set
        :return:
        """
        if self.equal(key, value):
            return self.set(**{key: new_value})

        return False

    def not_equal_then_set(self, key: str, value, new_value=None) -> bool:
        """
            If a setting does NOT equal a value, set it to a new value.
        :param key: setting key
        :param value: value to compare
        :param new_value: new value to set
        :return:
        """
        if self.not_equal(key, value):
            if new_value is None:
                return self.set(**{key: value})
            return self.set(**{key: new_value})

        return False
