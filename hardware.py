import shutil
import psutil


def check_disk_space():
    """Returns true if free space on selected disk is more than 20%"""
    disk = str(input("Enter drive letter or 'quit': ").upper() + ":")
    if disk == 'QUIT:':
        print("User ended space test.")
    else:
        try:
            disk_specs = shutil.disk_usage(disk)
            free_space = disk_specs.free / disk_specs.total * 100
            if free_space > 20:
                print(f"{disk} drive free space PASSED!")
            else:
                print(f"{disk} drive free space LOW!")
        except FileNotFoundError:
            print(f"Apparently, the {disk} drive does not exist!\n")
            check_disk_space()


def check_cpu_usage():
    """Returns true if CPU is used less than 75% capacity"""
    usage = psutil.cpu_percent(1)
    return usage < 75


def main():

    print("\nRunning hardware tests..")
    print("\nChecking disk space..")
    check_disk_space()

    print("\nChecking CPU usage..")
    cpu_ok = check_cpu_usage()
    if not check_cpu_usage():
        print("--CPU usage is high!")
    else:
        print("--CPU usage seems fine!")
