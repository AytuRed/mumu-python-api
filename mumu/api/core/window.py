#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 15:14
# @Author : wlkjyy
# @File : window.py
# @Software: PyCharm



class Window:

    def __init__(self, utils):
        self.utils = utils

    def show(self) -> bool:
        """
            Show the emulator window.
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['show_window'])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def hidden(self) -> bool:
        """
            Hide the emulator window.
        :return:
        """
        self.utils.set_operate('control')
        ret_code, retval = self.utils.run_command(['hide_window'])

        if ret_code == 0:
            return True

        raise RuntimeError(retval)

    def layout(self, x: int = None, y: int = None, width: int = None, height: int = None) -> bool:
        """
            Set the emulator window position and size.
        :param x: window X position (origin at top-left of the screen)
        :param y: window Y position (origin at top-left of the screen)
        :param width: window width
        :param height: window height
        :return:
        """
        self.utils.set_operate('control')
        args = ['layout_window']

        if x is not None:
            args.append('-px')
            args.append(str(x))

        if y is not None:
            args.append('-py')
            args.append(str(y))

        if width is not None:
            args.append('-width')
            args.append(str(width))

        if height is not None:
            args.append('-height')
            args.append(str(height))

        if len(args) == 1:
            raise RuntimeError('The layout method must have at least one parameter')

        ret_code, retval = self.utils.run_command(args)
        if ret_code == 0:
            return True

        raise RuntimeError(retval)
