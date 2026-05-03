#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 19:35
# @Author : wlkjyy
# @File : constant.py
# @Software: PyCharm
import os
import random


class MacAddress:

    @staticmethod
    def random() -> str:
        """
            Generate a random MAC address.
        :return:
        """
        mac = [random.randint(0x00, 0xff) for _ in range(6)]
        return ':'.join(map(lambda x: "%02x" % x, mac))


class IMEI:

    @staticmethod
    def random() -> str:
        """
            Generate a random IMEI.

            Source: chatgpt-3.5
        :return:
        """
        # Generate TAC (first 8 digits)
        tac = f"{random.randint(10 ** 5, 10 ** 6 - 1):06d}"

        # Generate FAC (next 2 digits)
        fac = f"{random.randint(0, 99):02d}"

        # Generate SNR (next 6 digits)
        snr = f"{random.randint(10 ** 5, 10 ** 6 - 1):06d}"

        # Concatenate parts
        imei_base = tac + fac + snr

        # Calculate Check Digit (SP)
        def calculate_check_digit(imei):
            digits = list(map(int, imei))
            odd_digits = digits[0::2]
            even_digits = [sum(divmod(2 * d, 10)) + 2 * d // 10 for d in digits[1::2]]
            total = sum(odd_digits + even_digits)
            return (10 - total % 10) % 10

        check_digit = calculate_check_digit(imei_base)

        # Construct full IMEI
        imei = imei_base + str(check_digit)

        return imei


class IMSI:

    @staticmethod
    def random() -> str:
        """
            Generate a random IMSI.
        :return:
        """
        mcc = random.choice(['302', '310', '334', '460'])  # Example MCCs for demonstration

        # MNC (Mobile Network Code, 2 or 3 digits)
        mnc = f"{random.randint(0, 999):03d}"[:2]  # Random 2-digit MNC

        # MSIN (Mobile Subscriber Identification Number, 10 digits)
        msin = f"{random.randint(0, 10 ** 10 - 1):010d}"

        # Concatenate parts
        imsi = mcc + mnc + msin

        return imsi


class AndroidID:

    @staticmethod
    def random() -> str:
        """
            Generate a random Android ID.
        :return:
        """
        return ''.join(random.choices('0123456789abcdef', k=16))


class PhoneNumber:

    @staticmethod
    def random() -> str:
        """
            Generate a random phone number.
        :return:
        """
        prefix = random.choice(['130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
                                '147', '150', '151', '152', '153', '155', '156', '157', '158', '159',
                                '186', '187', '188', '189', '199'])

        return prefix + ''.join(random.choices('0123456789', k=8))


class GPU:
    # High-end model
    TOP_MODEL = 'Adreno (TM) 740'

    # Mid-range model
    MIDDLE_MODEL = 'Adreno (TM) 640'

    # Low-end model
    LOW_MODEL = 'Adreno (TM) 530'


class AndroidKey:
    # Menu key
    KEYCODE_MENU = 1

    # Home (back to desktop)
    KEYCODE_HOME = 3

    # Back key
    KEYCODE_BACK = 4

    # Call key
    KEYCODE_CALL = 5

    # End-call key
    KEYCODE_ENDCALL = 6

    # Search key
    KEYCODE_SEARCH = 84

    # Camera shutter key
    KEYCODE_CAMERA = 27

    # Camera focus key
    KEYCODE_FOCUS = 80

    # Power key
    KEYCODE_POWER = 26

    # Notification key
    KEYCODE_NOTIFICATION = 83

    # Mute key
    KEYCODE_MUTE = 91

    # Speaker mute key
    KEYCODE_VOLUME_MUTE = 164

    # Volume up key
    KEYCODE_VOLUME_UP = 24

    # Volume down key
    KEYCODE_VOLUME_DOWN = 25

    # Enter key
    KEYCODE_ENTER = 66

    # ESC key
    KEYCODE_ESCAPE = 111

    # D-Pad center
    KEYCODE_DPAD_CENTER = 23

    # D-Pad up
    KEYCODE_DPAD_UP = 19

    # D-Pad down
    KEYCODE_DPAD_DOWN = 20

    # D-Pad left
    KEYCODE_DPAD_LEFT = 21

    # D-Pad right
    KEYCODE_DPAD_RIGHT = 22

    # Delete / backspace
    KEYCODE_DEL = 67

    # TAB
    KEYCODE_TAB = 61

    # Zoom-in key
    KEYCODE_ZOOM_IN = 168

