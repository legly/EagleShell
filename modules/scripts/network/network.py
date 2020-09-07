#!/usr/bin/python3

from assets.banners import network_banner
from assets.properties import clear_screen
from assets.designs import logo, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
import os


class Network:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print(network_banner)
            print(author)
            print('Scripts:')
            print('\n\t1): MAChanger - MAC Address Changer')
            print('\t2): ARPSpoof - ARP Spoofer')
            print('\t3): PacketSniff - Packet Sniffer')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                network_select = input(eagleshell_prefix).lower()
                if network_select == '1':
                    from modules.scripts.network.machanger import MAChanger
                    MAChanger()
                elif network_select == '2':
                    from modules.scripts.network.arpspoof import ARPSpoof
                    ARPSpoof()
                elif network_select == '3':
                    from modules.scripts.network.packetsniff import PacketSniff
                    PacketSniff()
                elif network_select == 'z':
                    from ..scripts import Scripts
                    Scripts()
                elif network_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
