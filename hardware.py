import shutil
import psutil
import get_valid_drives as gvd


def check_disk_space():
    """Returns true if free space on selected disk is more than a certain percentage"""
    percentage_check = 20
    disks = gvd.get_valid_drives()
    print(f"Checking for at least {percentage_check}% free space on each disk..")
    for disk in disks:
        try:
            disk_specs = shutil.disk_usage(disk)
            free_space = disk_specs.free / disk_specs.total * 100
            if free_space > percentage_check:
                print(f"{disk} drive PASSED!")
            else:
                print(f"{disk} drive free space LOW!")
        except FileNotFoundError:
            print(f"Apparently, the {disk} drive does not exist!\n")
            check_disk_space()


def check_cpu_usage():
    """Returns true if CPU is used less than a certain capacity"""
    percentage_check = 75
    print(f"\nChecking CPU usage is below {percentage_check}%..")
    usage = psutil.cpu_percent(1)
    return usage < percentage_check


def main():

    print("\nRunning hardware tests..")
    print("-" * 25)
    check_disk_space()

    cpu_ok = check_cpu_usage()
    if not cpu_ok:
        print("--CPU usage is high!")
    else:
        print("--CPU usage seems fine!")
