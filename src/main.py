from extra.error_handling import error_handle
from auth.create_tas import create_tas


def main():
    raw_return = create_tas()
    error_handle(raw_return)
    tas = raw_return[1]
    






if __name__ == "__main__":
    main()