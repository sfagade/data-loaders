# This is a sample Python script.
import sys
from configuration import init_logger


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    log = init_logger("Main function:")

    log.info("Running app with {0} arguments.".format(sys.argv))
    process_for = sys.argv[1] if len(sys.argv) > 1 else "alarinka"

    print_hi('PyCharm')

