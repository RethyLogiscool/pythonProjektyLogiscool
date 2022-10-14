import platform
import psutil, os, time

p = psutil.Process(os.getpid())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(p.create_time())))