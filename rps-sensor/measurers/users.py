import psutil

from measurers.userdata import UserData


def get_users_count():
    return len(psutil.users())


def measure_users():
    udata = UserData()
    udata.users_count = get_users_count()
    return udata
