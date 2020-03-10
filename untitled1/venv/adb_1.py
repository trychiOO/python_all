# import subprocess
#
#
# subprocess.Popen(["cat test.txt"])

import subprocess

returnCode = subprocess.call('adb devices')

print (returnCode)