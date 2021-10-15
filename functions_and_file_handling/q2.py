"""
#
# File        : q2
# Created     : 15/10/21 9:50 AM
# Author      : R. Aravind
# Version     : v1.0.0
# Licencing   : (C) 2021 Aravind Rajesh Kanna, LYIT
                Available under GNU Public License (GPL)
# Credits    :
# Maintainer  :
# Description : Prints the time taken to perform the encryption
#
"""

import timeit


if __name__ == '__main__':
    '''

           Main method of application 

           Prints the time taken to encrypt password

           Parameters:

            none

           Returns:

            none

        '''

    setup_code = "import crypt"
    statement = "crypt.crypt('jnsvfi09osapjfsp0f9')"

    print(timeit.timeit(setup=setup_code, stmt=statement, number=1))
