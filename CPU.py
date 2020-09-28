import psutil
from datetime import datetime
from time import sleep
import statistics
import time

cpu_usage = []
print ("CPU usage \t\tTime")

for i in range(121):
    cpu_usage.append(psutil.cpu_percent())
    print("CPU %:",cpu_usage[i], " Time: ", datetime.now()) 
    sleep(5)

del cpu_usage[0]

print(cpu_usage)
print("Average : ", statistics.mean(cpu_usage))
