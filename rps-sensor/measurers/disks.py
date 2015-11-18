import psutil


def get_disk_partitions():
    return filter(lambda d: d[2] != '', psutil.disk_partitions(all=False))


def get_disk_usages(partitions):
    

