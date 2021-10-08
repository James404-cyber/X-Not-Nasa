
import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from libnologin import starting_menu
    starting_menu()
elif bit == '32bit':
    from libnologin import starting_menu
    starting_menu()
