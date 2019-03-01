# pip install configparser
# Requirement already satisfied: psutil in
# ./.pyenv/versions/3.7.2/lib/python3.7/site-packages (5.5.1)
# Requirement already satisfied: configparser in
# ./.pyenv/versions/3.7.2/lib/python3.7/site-packages (3.7.3)
# I don't know why parser doesn't work


import time
# import configparser
import psutil
import json
# import os.path
import datetime


class Mon:
    count = 1

    def hard():

        if outputlog == "json":
            ts = time.ctime()
            cpu = psutil.cpu_percent()
            mem_total = psutil.virtual_memory().total / 1024 ** 3
            mem_used = psutil.virtual_memory().used / 1024 ** 3
            io = psutil.disk_io_counters(perdisk=False)
            net = psutil.net_io_counters()
            timestamp = datetime.datetime.now().strftime(ts.TIME_FORMAT)
            with open("mon.json", "a") as out:
                json.dumps({'SNAPSHOT ' + str(Mon.count): timestamp,
                            'CPU_LOAD_%': cpu,
                            'MEM_TOTAL_IN_GB':
                                float("{:.2f}".format(mem_total)),
                            'MEM_USED_IN_GB': float("{:.2f}".format(mem_used)),
                            'READ_COUNT': io[0],
                            'WRITE_COUNT': io[1],
                            'BYTES_RECEIVED': net}, out, indent=1)

            Mon.count = Mon.count + 1

        elif outputlog == "txt":
            cpu = "(CPUload " + str(psutil.cpu_percent(interval=1)) + ")"
            mem = str(psutil.Process().memory_info())
            vmem = str(psutil.virtual_memory().used)
            io = str(psutil.disk_io_counters())
            net = str(psutil.net_if_addrs())
            ts = time.ctime()
            ss = "SNAPSHOT"
            log = open("mon.log", "a")
            log.write(ss + " " + str(Mon.count) + ": " + ts + " " + cpu)
            log.write(" " + mem + " " + vmem + " " + io + " " + net + "\n")
            log.close()
            Mon.count = Mon.count + 1

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

    if "json" in line:
        outputlog = "json"

    if "settings" and "interval" in line:
        intervalmin = int(line[11:])

for i in range(intervalmin):
    Mon.hard()
    print("Date and time are", time.ctime())
    time.sleep(intervalmin * 0.02)

conf.close()
exit(0)
