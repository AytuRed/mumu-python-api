#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/7/29 14:44
# @Author : wlkjyy
# @File : Network.py
# @Software: PyCharm
from mumu.api.setting.setting import Setting


class Network:

    def __init__(self, utils):
        self.utils = utils

    def get_bridge_card(self):
        """
            Get all bridge adapters.
        :return:
        """
        card = Setting(self.utils).get('net_bridge_card.list')
        if isinstance(card, list):
            return card

        if not isinstance(card, str):
            return []

        card = card.strip()
        if card.startswith('[') and card.endswith(']'):
            card = card[1:-1]

        if not card:
            return []

        return [item.strip() for item in card.split(',')]

    def nat(self):
        """
            Set the network to NAT mode.
        :return:
        """
        return Setting(self.utils).set(
            net_bridge_open=False
        )

    def bridge(self, enable: bool = True, net_bridge_card: str = None):
        """
            Enable or disable the bridge.
        :param enable: whether to enable
        :param net_bridge_card: bridge adapter to use
        :return:
        """
        return Setting(self.utils).set(
            net_bridge_open=enable,
            net_bridge_card=net_bridge_card
        )

    def bridge_dhcp(self):
        """
            Configure the bridge to use DHCP.
        :return:
        """
        return Setting(self.utils).set(
            net_bridge_ip_mode='dhcp'
        )

    def bridge_static(self, ip_addr: str, subnet_mask: str, gateway: str, dns1: str = '8.8.8.8', dns2: str='114.114.114.114'):
        """
            Configure the bridge with a static IP.
        :param ip_addr: IP address
        :param subnet_mask: subnet mask
        :param gateway: gateway
        :param dns1: DNS1
        :param dns2: DNS2
        :return:
        """
        return Setting(self.utils).set(
            net_bridge_ip_mode='static',
            net_bridge_ip_addr=ip_addr,
            net_bridge_subnet_mask=subnet_mask,
            net_bridge_gateway=gateway,
            net_bridge_dns1=dns1,
            net_bridge_dns2=dns2
        )
