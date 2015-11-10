import psutil

from measurers.memdata import MemoryData


def measure_memory():
    mdata = MemoryData()
    mdata.virtual = mdata.virtual(*measure_virtual())
    mdata.swap = mdata.swap(*measure_swap())
    return mdata


def measure_virtual():
    mem = psutil.virtual_memory()
    return mem[0], mem[1]


def measure_swap():
    mem = psutil.swap_memory()
    return mem[0], mem[2]
