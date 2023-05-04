from auth.create_tas import create_tas

import sys

class Twitter():
    def __init__(self):
        self.tas = None
        self.auth_uid = 0
        self.auth_username = ""
    
    # this will end the program when the the raw_return[0] indicates an error
    def error_handle(raw_return):
        if raw_return[0] == 1:
            sys.exit(raw_return[1][0])

    # create twitter authorized session object
    def create_tas(self):
        raw_return = create_tas()
        self.error_handle(raw_return)

        self.tas = raw_return[1][0]
        self.auth_uid = raw_return[1][1]
        self.auth_username = raw_return[1][2]