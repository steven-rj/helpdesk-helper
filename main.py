import hardware as hardware
import network as network
import file_search
import time
import sys


def display_diagnostics_menu():

    diagnostics = ["run all tests", "check hardware", "check network", "return to main menu"]

    print("\nAvailable Diagnostics:")
    print("-" * 22)

    for i, test in enumerate(diagnostics, 1):
        print(f"{i}: {test}")
    option_num = int(input("\nChoose option by number: "))

    if option_num == 1:
        hardware.main()
        time.sleep(1)
        network.main()
    elif option_num == 2:
        hardware.main()
    elif option_num == 3:
        network.main()
    elif option_num == 4:
        display_main_menu

    display_main_menu()


def display_utilities_menu():

    utilities = ["file search", "return to main menu"]

    print("\nAvailable Utilities")
    print("-" * 19)

    for i, option in enumerate(utilities, 1):
        print(f"{i}: {option}")
    option_num = int(input("\nChoose option by number: "))

    if option_num == 1:
        file_search.main()

    display_main_menu()


def display_main_menu():

    options = ["Diagnostics", "Utilities", "Exit"]
    option_num = 0

    print("\n====================")
    print("Helpdesk Helper v0.5")
    print("====================")

    for i, option in enumerate(options, 1):
        print(f"{i}: {option}")

    option_num = int(input("\nChoose option by number: "))

    if option_num == 1:
        print("\nLoading Diagnostic Tests..")
        time.sleep(1)
        display_diagnostics_menu()
    elif option_num == 2:
        print("\nLoading Utilities..")
        time.sleep(1)
        display_utilities_menu()
    elif option_num == 3:
        sys.exit()
    else:
        print("Please select a valid option")
        time.sleep(1)
        display_main_menu()

if __name__ == "__main__":
    display_main_menu()
