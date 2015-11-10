import psutil

from measurers.cpudata import CpuData
from sensor import CONFIG


def measure_cpu():
    data = CpuData()
    data.usage = measure_cpu_usage()
    data.times = data.times(*measure_cpu_times())
    data.cpu_count = measure_cpu_count()
    return data


def measure_cpu_usage():
    return psutil.cpu_percent(interval=CONFIG.CPU_MEASURE_INTERVAL, percpu=True)


def measure_cpu_times():
    return psutil.cpu_times_percent(interval=CONFIG.CPU_MEASURE_INTERVAL, percpu=True)


def measure_cpu_count():
    return psutil.cpu_count
