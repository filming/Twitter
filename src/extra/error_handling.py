import sys

# this will end the program when the the raw_return[0] indicates an error
def error_handle(raw_return):
    if raw_return[0] == 1:
        sys.exit(raw_return[1][0])
