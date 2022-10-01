
from paths import FilePaths
from arp_table import show_arp_table

paths = FilePaths()

iosv_host = "192.168.140.2"
nxos_host = "172.20.129.2"

print(show_arp_table(host=nxos_host, platform_id="cisco_ios", credential_id="gns3"))

