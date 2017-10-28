import sys
import os
import time
import subprocess
import re

def connect(ssid, password):
    f = open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w+')

    f.write(
    '''
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
        ssid="%s"
        psk="%s"
        key_mgmt=WPA-PSK
    }
    ''' % (ssid, password)
    )
    f.close()

    os.system('sudo ifdown wlan0')
    os.system('sudo ifup wlan0')
    time.sleep(5)
    iwconfig_result = subprocess.Popen(
        ['iwconfig', 'wlan0'],
        stdout=subprocess.PIPE,
        )
    grep_result = subprocess.Popen(
        ['grep', 'ESSID'],
        stdin=iwconfig_result.stdout,
    )
    print(ssid)
    if 'ESSID:"%s"'%(ssid) in str(grep_result.stdout):
        return True
    else:
        return False


if __name__ == '__main__':
    print('Hello World!')
    connect('lan', 'wjdflkasdjflk')