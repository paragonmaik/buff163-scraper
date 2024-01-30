from commands.reader import read_flags, get_float_type_command
from scraper.scraper import search_skins


def main():
    read_flags()

    search_skins(
        get_float_type_command("-p"),
        get_float_type_command("-v"),
        get_float_type_command("-q"),
        get_float_type_command("-b"),
    )
    while True:
        pass


if __name__ == "__main__":
    main()
