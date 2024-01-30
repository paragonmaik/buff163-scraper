from commands.reader import read_flags, USED_COMMANDS_LIST
from scraper.scraper import search_skins


def get_float_type_command(flag: str) -> float:
    if flag in USED_COMMANDS_LIST:
        return float(USED_COMMANDS_LIST[flag])
    return 0


def main():
    read_flags()

    # TODO: move to commands module
    filtered_pct = get_float_type_command("-p")
    filtered_price_diff = get_float_type_command("-v")
    filtered_ask = get_float_type_command("-q")
    filtered_bid = get_float_type_command("-b")
    print(
        filtered_pct,
        filtered_price_diff,
        filtered_ask,
        filtered_bid,
    )

    search_skins(
        filtered_pct,
        filtered_price_diff,
        filtered_ask,
        filtered_bid,
    )
    while True:
        pass


if __name__ == "__main__":
    main()
