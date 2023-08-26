"""A scripts specific for Ukrainian schools."""
from check_site import search_text, logging
from shorteners import ukr_schools_shorten as shorten
import csv
import time

def search(text: str, url: str) -> int:
    """Run the script.

    Args:
        text: Text to search.
        url: Url to search.

    Returns:
        int: ЄДРПОУ of the school if text is present on the page,
        0 otherwise.
    """
    page_text = "429toomanyrequests"
    while "429toomanyrequests" in page_text:
        found, page_text = search_text(text, url, shorten)
        if found:
            logging.info(f"'{text}' is present on the page '{url}'.")
            return int(url.split("/")[-1])
        if "429toomanyrequests429toomanyrequestsopenresty" in page_text:
            logging.error("Too many requests. Waiting 10 seconds.")
            time.sleep(10)
            continue
        logging.warning(f"'{text}' is not present on the page '{url}'.")
        logging.debug(f"Shortened text: '{shorten(text)}'.")
        logging.debug(f"Text from the page: \n\nSTART\n{page_text}\nEND\n\n")
        return 0
    return 0


def write_nums_to_csv(nums: list[tuple[str, str, int]]) -> None:
    """Write nums to csv file.

    Args:
        nums: List of tuples (text, url, num).
    """
    with open("nums.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(nums)


def parse_schools(file: str) -> None:
    """Open csv file and search each text on the corresponding url.

    The csv format is:
    <text>,<url>

    Args:
        file: Path to csv file.

    Raises:
        KeyboardInterrupt: If the user presses Ctrl+C.
    """
    nums: list[tuple[str, str, int]] = []
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)
        try:
            for row in reader:
                num = search(row[0], row[1])
                if num:
                    logging.info(f"ЄДРПОУ: {num}")
                nums.append((row[0], row[1], num))
                time.sleep(2)
        except KeyboardInterrupt:
            logging.error("Keyboard interrupt.")
            write_nums_to_csv(nums)
            raise
    write_nums_to_csv(nums)
