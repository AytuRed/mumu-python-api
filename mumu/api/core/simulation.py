#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 19:25
# @Author : wlkjyy
# @File : simulation.py
# @Software: PyCharm



from mumu.constant import MacAddress, IMEI, IMSI, AndroidID, PhoneNumber, GPU
from mumu.api.setting.setting import Setting


class Simulation:

    def __init__(self, utils):
        self.utils = utils

    def __action(self, sk: str, sv: str) -> bool:
        self.utils.set_operate('simulation')
        ret_code, retval = self.utils.run_command(['-sk', sk, '-sv', sv])
        if ret_code == 0:
            return True
        raise RuntimeError(retval)

    def mac_address(self, mac: str = None) -> bool:
        """
            Set the emulator MAC address.
        :param mac: MAC address to set
        :return:
        """
        if mac is None:
            mac = MacAddress.random()

        return self.__action('mac_address', mac)

    def imei(self, imei: str = None) -> bool:
        """
            Set the emulator IMEI.
        :param imei: IMEI to set
        :return:
        """
        if imei is None:
            imei = IMEI.random()

        return self.__action('imei', imei)

    def imsi(self, imsi: str = None) -> bool:
        """
            Set the emulator IMSI.
        :param imsi: IMSI to set
        :return:
        """
        if imsi is None:
            imsi = IMSI.random()

        return self.__action('imsi', imsi)

    def android_id(self, android_id: str = None) -> bool:
        """
            Set the emulator Android ID.
        :param android_id: Android ID to set
        :return:
        """
        if android_id is None:
            android_id = AndroidID.random()

        return self.__action('android_id', android_id)

    def model(self, model: str) -> bool:
        """
            Set the emulator device model.
        :param model: device model to set
        :return:
        """
        return self.__action('model', model)

    def brand(self, brand: str) -> bool:
        """
            Set the emulator brand.
        :param brand: brand to set
        :return:
        """
        return self.__action('brand', brand)

    def solution(self, solution: str) -> bool:
        """
            Set the emulator hardware solution.
        :param solution: hardware solution to set
        :return:
        """
        return self.__action('solution', solution)

    def phone_number(self, phone_number: str = None) -> bool:
        """
            Set the emulator phone number.
        :param phone_number: phone number to set
        :return:
        """
        if phone_number is None:
            phone_number = PhoneNumber.random()

        return self.__action('phone_number', phone_number)

    def gpu_model(self, gpu_model_name: str = "GeForce GTX 4090 Ti", top_model=False, middle_model=False,
                  low_model=False) -> bool:
        """
            Set the emulator GPU model.
        :param gpu_model_name: custom GPU model
        :param top_model: use the high-end GPU preset
        :param middle_model: use the mid-range GPU preset
        :param low_model: use the low-end GPU preset
        :return:
        """
        if top_model:
            return Setting(self.utils).set(
                gpu_mode="high",
                gpu_model__custom=GPU.TOP_MODEL
            )

        if middle_model:
            return Setting(self.utils).set(
                gpu_mode="middle",
                gpu_model__custom=GPU.MIDDLE_MODEL
            )

        if low_model:
            return Setting(self.utils).set(
                gpu_mode="low",
                gpu_model__custom=GPU.LOW_MODEL
            )

        return Setting(self.utils).set(
            gpu_mode="custom",
            gpu_model__custom=gpu_model_name
        )
