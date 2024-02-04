# Python 3.x
from memory_profiler import profile
from memory_profiler import memory_usage
from memory_profiler import LogFile
import sys

# mem_usage = memory_usage(-1, interval=.2, timeout=1)
# print(mem_usage)
fp=open('memory_profiler.log','w+')
@profile(stream=fp)
def myfunc():
    a = []
    for i in range(1000):
        a.append(i)

myfunc()
sys.stdout = LogFile("memory_profile_log", reportIncrementFlag=False)