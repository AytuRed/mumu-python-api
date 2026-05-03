#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 20:54
# @Author : wlkjyy
# @File : screen.py.py
# @Software: PyCharm


from mumu.api.setting.setting import Setting


class Screen:

    def __init__(self, utils):
        self.utils = utils

    def resolution(self, width: int, height: int):
        """
            Change the resolution.
        :param width:
        :param height:
        :return:
        """
        return Setting(self.utils).set(
            resolution_height__custom=height,
            resolution_width__custom=width
        )

    def resolution_mobile(self):
        """
            Set the mobile-phone resolution preset.
        :return:
        """
        self.resolution(width=1080, height=1920)
        self.dpi(480)

    def resolution_tablet(self):
        """
            Set the tablet resolution preset.
        :return:
        """
        self.resolution(width=1920, height=1080)
        self.dpi(280)

    def resolution_ultrawide(self):
        """
            Set the ultra-wide resolution preset.
        :return:
        """
        self.resolution(width=3200, height=1440)
        self.dpi(400)

    def dpi(self, dpi: int):
        """
            Change the DPI.
        :param dpi:
        :return:
        """
        return Setting(self.utils).set(
            resolution_dpi__custom=dpi
        )

    def brightness(self, brightness: int):
        """
            Set the emulator brightness.
        :param brightness: brightness value 1-100
        :return:
        """
        brightness = max(1, min(100, brightness))

        return Setting(self.utils).set(
            screen_brightness=brightness
        )

    def max_frame_rate(self, frame_rate: int = 60):
        """
            Set the emulator maximum frame rate.
        :param frame_rate: max frame rate (1-240)
        :return:
        """
        frame_rate = max(1, min(240, frame_rate))

        return Setting(self.utils).set(
            max_frame_rate=frame_rate
        )

    def dynamic_adjust_frame_rate(self, enable: bool, dynamic_low_frame_rate_limit: int = 15):
        """
            Enable or disable dynamic frame-rate adjustment.
        :param enable: whether to enable
        :param dynamic_low_frame_rate_limit: target frame rate when this emulator is not the active window
        :return:
        """
        return Setting(self.utils).set(
            dynamic_adjust_frame_rate=enable,
            dynamic_low_frame_rate_limit=dynamic_low_frame_rate_limit
        )

    def vertical_sync(self, enable: bool):
        """
            Enable or disable vertical sync.
        :param enable: whether to enable
        :return:
        """
        return Setting(self.utils).set(
            vertical_sync=enable
        )

    def show_frame_rate(self, enable: bool):
        """
            Show or hide the frame-rate overlay.
        :param enable: whether to show
        :return:
        """
        return Setting(self.utils).set(
            show_frame_rate=enable
        )

    def window_auto_rotate(self, enable: bool):
        """
            Enable or disable window auto-rotation.

            When enabled, the emulator window rotates automatically based on the running app.
        :param enable: whether to enable
        :return:
        """
        return Setting(self.utils).set(
            window_auto_rotate=enable
        )
