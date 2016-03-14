import psutil

from utils.configuration import CONFIG


def measure_cpu():
    data = {}
    data['usage'] = measure_cpu_usage()
    data['times'] = [tuple(times) for times in measure_cpu_times()]
    data['cpu_count'] = measure_cpu_count()
    return data


def measure_cpu_usage():
    return psutil.cpu_percent(interval=CONFIG.CPU_MEASURE_INTERVAL, percpu=True)


def measure_cpu_times():
    return psutil.cpu_times_percent(interval=CONFIG.CPU_MEASURE_INTERVAL, percpu=True)


def measure_cpu_count():
    return psutil.cpu_count()
