# pip install psutil configparser
# Requirement already satisfied: psutil in
# ./.pyenv/versions/3.7.2/lib/python3.7/site-packages (5.5.1)
# Requirement already satisfied: configparser in
# ./.pyenv/versions/3.7.2/lib/python3.7/site-packages (3.7.3)
# I don't know why parser doesn't work


import time
# import configparser
import psutil


class Mon:
    count = 1

    def hard():
        cpu = "(CPUload " + str(psutil.cpu_percent(interval=1)) + ")"
        mem = str(psutil.Process().memory_info())
        vmem = str(psutil.virtual_memory().used)
        io = str(psutil.disk_io_counters())
        net = str(psutil.net_if_addrs())
        ts = time.ctime()
        ss = "SNAPSHOT"
        if outputlog == "txt":
            log = open("mon.log", "a")
            log.write(ss + " " + str(Mon.count) + ": " + ts + " " + cpu)
            log.write(" " + mem + " " + vmem + " " + io + " " + net + "\n")

            Mon.count = Mon.count + 1
            log.close()
        else:
            print("This output isn't exist. "
                  "Our team is working on this feature......")
            exit(1)


# Workaround configparser
conf = open("app.conf", "r")
for line in conf:
    #    print(line)
    if "txt" in line:
        outputlog = "txt"
    if "settings" and "interval" in line:
        intervalmin = int(line[11:])

print("intervalmin= ", intervalmin)

for i in range(0, intervalmin):
    Mon.hard()
    print("Date and time are", time.ctime())
    time.sleep(60)

conf.close()
exit(0)
