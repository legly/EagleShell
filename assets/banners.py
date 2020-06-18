#!/usr/bin/python3

from assets.properties import version
from assets.properties import total_scripts

payloads_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Payloads | [Total] 0 Payloads Available'
listeners_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Listeners | [Total] 0 Listeners Available'
scripts_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Scripts | [Total] ' + total_scripts +' Scripts Available'
scanning_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning'
enumeration_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Scripts | [Option] Enumeration'
privilege_escalation_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Scripts | [Option] Privilege Escalation'
miscellaneous_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous'
rsgen_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] RSGEN'
machanger_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] MACHANGER'
eagleye_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] EAGLEYE'
eaglscan_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] EAGLESCAN'
pgen_banner = '\u001b[36;1m [Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] PGEN'