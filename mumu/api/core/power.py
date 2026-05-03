#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 15:05
# @Author : wlkjyy
# @File : power.py
# @Software: PyCharm



class Power:

    def __init__(self, utils):
        self.utils = utils

    def start(self, package: str = None) -> bool:
        """
            Start the emulator.
        :param package: optional package name to auto-launch on start
        :return:
        """
        self.utils.set_operate('control')
        args = ['launch']
        if package is not None:
            args.extend(['-pkg', package])

        ret_code, retval = self.utils.run_command(args)
        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def shutdown(self):
        """
            Shut down the emulator.
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['shutdown'])
        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def restart(self):
        """
            Restart the emulator.
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['restart'])
        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def stop(self):
        """
            Stop an emulator.
        :return:
        """
        return self.shutdown()

    def reboot(self):
        """
            Reboot an emulator.
        :return:
        """
        return self.restart()
