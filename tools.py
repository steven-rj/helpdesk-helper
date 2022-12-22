import os
import sys
import subprocess

tools = {
    "defrag": "C:\\Windows\\system32\\dfrgui.exe",
    "cleaner": "C:\\Windows\\system32\\cleanmgr.exe"
}


def tool_check():
    """Runs a test to make sure each utility in tools dict is valid"""

    for k, v in tools.items():
        if not os.path.isfile(v):
            print(f"{k} tool not found!")
        else:
            print(f"{k} tool found!")


def run_defrag():
    """Runs the Disk Defrag utility"""
    result = subprocess.run(tools["defrag"], capture_output=True)
    if result.returncode != 0:
        print(result.stderr.decode())
    else:
        print(result.stdout.decode())


def run_cleaner():
    """Runs the Disk Cleaner utility"""
    subprocess.run(tools["cleaner"])


if __name__ == "__main__":
    run_defrag()
