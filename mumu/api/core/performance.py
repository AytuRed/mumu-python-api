#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 21:58
# @Author : wlkjyy
# @File : performance.py
# @Software: PyCharm
from mumu.api.setting.setting import Setting


class Performance:

    def __init__(self, utils):
        self.utils = utils

    def set(self, cpu_num: int = 1, mem_gb: int = 2):
        """
            Set emulator performance.
        :param cpu_num: number of CPU cores
        :param mem_gb: memory size in GB
        :return:
        """
        cpu_num = max(1, min(16, cpu_num))

        return Setting(self.utils).set(
            performance_mode='custom',
            performance_cpu__custom=cpu_num,
            performance_mem__custom=mem_gb
        )

    def cpu(self, cpu_num: int):
        """
            Set the emulator CPU core count.
        :param cpu_num: number of CPU cores
        :return:
        """
        cpu_num = max(1, min(16, cpu_num))

        return Setting(self.utils).set(
            performance_mode='custom',
            performance_cpu__custom=cpu_num
        )

    def memory(self, mem_gb: int):
        """
            Set the emulator memory size.
        :param mem_gb: memory size in GB
        :return:
        """
        mem_gb = max(1, mem_gb)

        return Setting(self.utils).set(
            performance_mode='custom',
            performance_mem__custom=mem_gb
        )

    def force_discrete_graphics(self, enable: bool):
        """
            Force use of the discrete GPU.
        :param enable: whether to enable
        :return:
        """
        return Setting(self.utils).set(
            force_discrete_graphics=enable
        )

    def renderer_strategy(self, auto=True, dis=False, perf=False):
        """
            VRAM usage strategy.
        :param auto: auto tuning
        :param dis: better visual quality
        :param perf: lower resource usage
        :return:
        """
        if dis:
            return Setting(self.utils).set(
                renderer_strategy='dis'
            )

        if perf:
            return Setting(self.utils).set(
                renderer_strategy='perf'
            )

        if auto:
            return Setting(self.utils).set(
                renderer_strategy='auto'
            )

    def disk_readonly(self, enable: bool = True):
        """
            Set whether the system disk is read-only.
        :param enable: whether read-only
        :return:
        """
        return Setting(self.utils).set(
            system_disk_readonly=enable
        )

    def disk_writable(self):
        """
            Make the system disk writable.
        :return:
        """
        return self.disk_readonly(False)
