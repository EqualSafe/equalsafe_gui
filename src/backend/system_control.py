'''
ALL OF THE SIMPLE UTILITES/COMMANDS IN ONE PLACE!
'''
import os

def reboot_device():
    os.system('reboot')

def enable_ssh():
    os.system('systemctl start sshd.service')

def disable_ssh():
    os.system('systemctl stop sshd.service')

