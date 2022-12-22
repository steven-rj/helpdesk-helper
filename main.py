import hardware as hardware
import network as network
import time


def display_menu():

    tests = ["run all tests", "check hardware", "check network"]

    print("Diagnostics:")
    for i, test in enumerate(tests, 1):
        print(f"{i}: {test}")
    test_num = int(input("Choose option by number: "))
    run_test(test_num)


def run_test(test_number):
    if test_number == 1:
        hardware.main()
        time.sleep(1)
        network.main()
    elif test_number == 2:
        hardware.main()
    elif test_number == 3:
        network.main()


if __name__ == "__main__":
    display_menu()
