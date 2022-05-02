import csv, os, time
from datetime import date
from datetime import datetime
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

up = 0.0
down = 0.0

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y--%H-%M-%S")

filename = str(dt_string) + ".csv"
print(filename)

f = open(filename, "w")

starttime=time.time()
interval = 30.0
while True:
    result = ping("1.1.1.1")
    f.write(str(str(datetime.now()) + ", " + str((1 if result else 0)) + "\n"))
    if result:
        up = up + 1.0
    else:
        down = down + 1.0


    print("Up: " + str(up))
    print("Down: " + str(down))
    print("Ratio: " +  str(up) + "/" +str(up+down) + " = " + str((up/(up+down))))
    print("Total Time Down: " + str(down * 30.0 / 60.0) + " minutes")


    time.sleep(interval - ((time.time() - starttime) % interval))



f.close()
