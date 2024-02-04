# Python 3.x
from guppy import hpy

heap = hpy()
heap.setref()
heap_status1 = heap.heap()
print("Heap Size before creating objects:", heap_status1.size, " bytes\n")
# print(heap_status1)
a = []
for i in range(1000):
    a.append(i)
heap_status2 = heap.heap()
print("Heap Size after creating objects : ", heap_status2.size, " bytes\n")
# print(heap_status2)