#!/usr/bin/python3

from assets.properties import version, total_scripts, total_settings
from assets.colors import *

scripts_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Total] ' + str(total_scripts) + ' Scripts Available\n'
settings_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Settings | [Total] ' + str(total_settings) + ' Settings Available\n'

scanning_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning\n'
enumeration_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Enumeration\n'
exploitation_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation\n'
privilege_escalation_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Privilege Escalation\n'
brute_force_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force\n'
network_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network\n'
web_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Web\n'
cryptography_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Cryptography\n'
miscellaneous_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous\n'

netscan_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] NetScan\n'
portscan_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] PortScan\n'

rsgen_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] RSGen\n'
pgen_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] PGen\n'

machanger_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] MaChanger\n'
arpspoof_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] ARPSpoof\n'
packetsniff_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] PacketSniff\n'

bruteftp_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BruteFTP\n'
brutessh_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BruteSSH\n'

linkextract_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Web | [Script] LinkExtract\n'
imgextract_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Web | [Script] IMGExtract\n'
subscan_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Web | [Script] SubScan\n'

hashing_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] Hashing\n'
exif_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] Exif\n'
crypt_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] Crypt\n'

update_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Settings | [Option] Update | [Script] Update\n'
setup_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Settings | [Option] Setup | [Script] Setup\n'
