#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 18:34
# @Author : wlkjyy
# @File : develop.py
# @Software: PyCharm




class AndroidEvent:

    def __init__(self, utils):
        self.utils = utils

    def __action(self, action_name: str) -> bool:
        """
            Execute an action.
        :param action_name: action name
        :return:
        """
        self.utils.set_operate("control")
        ret_code, ret_val = self.utils.run_command(['tool', 'func', '-n', action_name])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)

    def rotate(self) -> bool:
        """
            Rotate the screen.
        :return:
        """
        return self.__action("rotate")

    def rotates(self) -> bool:
        """
            Compatibility alias for rotate.
        :return:
        """
        return self.rotate()

    def go_home(self) -> bool:
        """
            Go to the home screen.
        :return:
        """
        return self.__action("go_home")

    def go_back(self) -> bool:
        """
            Go back.
        :return:
        """
        return self.__action("go_back")

    def top_most(self) -> bool:
        """
            Pin window on top.
        :return:
        """
        return self.__action("top_most")

    def fullscreen(self) -> bool:
        """
            Fullscreen.
        :return:
        """
        return self.__action("fullscreen")

    def shake(self) -> bool:
        """
            Shake the device.
        :return:
        """
        return self.__action("shake")

    def screenshot(self) -> bool:
        """
            Take a screenshot.
        :return:
        """
        return self.__action("screenshot")

    def volume_up(self) -> bool:
        """
            Volume up.
        :return:
        """
        return self.__action("volume_up")

    def volume_down(self) -> bool:
        """
            Volume down.
        :return:
        """
        return self.__action("volume_down")

    def volume_mute(self) -> bool:
        """
            Mute volume.
        :return:
        """
        return self.__action("volume_mute")

    def go_task(self) -> bool:
        """
            Press the Android recent-tasks key.
        :return:
        """
        self.utils.set_operate("adb")
        ret_code, ret_val = self.utils.run_command(['-c','go_task'])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)

    def location(self, lon: float, lat: float) -> bool:
        """
          Set the virtual GPS location.
        :param lon: longitude (float between -180 and 180)
        :param lat: latitude (float between -90 and 90)
        :return:
        """
        if lon < -180 or lon > 180:
            raise ValueError("The longitude range is incorrect")

        if lat < -90 or lat > 90:
            raise ValueError("The latitude range is incorrect")

        self.utils.set_operate("control")
        ret_code, ret_val = self.utils.run_command(['tool', 'location', '-lon', str(lon), '-lat', str(lat)])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)

    def gyro(self, x: float, y: float, z: float) -> bool:
        """
            Set virtual gyroscope values.
        :param x: x-axis
        :param y: y-axis
        :param z: z-axis
        :return:
        """
        self.utils.set_operate("control")
        ret_code, ret_val = self.utils.run_command(['tool', 'gyro', '-gx', str(x), '-gy', str(y), '-gz', str(z)])
        if ret_code == 0:
            return True

        raise RuntimeError(ret_val)
