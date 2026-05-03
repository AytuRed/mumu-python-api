#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 14:41
# @Author : wlkjyy
# @File : Driver.py
# @Software: PyCharm
from mumu.api.driver.bridge import Bridge


class Driver:

    def __init__(self, utils):
        self.utils = utils

    """
        Per the official docs, only the "network bridge" driver is supported for now.
    """

    @property
    def bridge(self):
        """
            Network bridge driver.
        :return:
        """

        return Bridge(self.utils)
