"""
#
# File        : q1
# Created     : 11/10/21 11:02 AM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : Prints the system info
#
"""


import platform
import os


def print_system_info():
    """

       print_system_info method of application

       Prints the system info

       Parameters:

        ""

       Returns:

        none

    """

    print(f"Machine         : {platform.machine()}")
    print(f"Node            : {platform.node()}")
    print(f"OS              : {platform.system()}")
    print(f"Current Path    : {os.path.abspath(os.getcwd())}")
    print(f"Architecture    : {platform.architecture()}")
    print(f"Platform        : {platform.platform()}")
    print(f"Mac Version     : {platform.mac_ver()}")


if __name__ == '__main__':
    '''

           Main method of application 

           Calls the system info printing func

           Parameters:

            none

           Returns:

            none

        '''

    print_system_info()
