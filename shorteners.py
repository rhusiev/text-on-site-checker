"""Shorten the text to remove human factor."""
import re


def shorten(text: str) -> str:
    """Shorten the text to remove human factor.

    Args:
        text: Text to shorten.

    Returns:
        str: Shortened text.
    """
    text = re.sub(r"\s+", "", text)
    text = (
        text.lower()
        .replace(" ", "")
        .replace("\n", "")
        .replace("\t", "")
        .replace("'", "")
        .replace("’", "")
        .replace("«", "")
        .replace("»", "")
        .replace("„", "")
        .replace("“", "")
        .replace('"', "")
        .replace(":", "")
        .replace(";", "")
        .replace(",", "")
        .replace(".", "")
        .replace("!", "")
        .replace("?", "")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
    )
    return text


def ukr_schools_shorten(text: str) -> str:
    """Shorten the text to remove human factor.

    This function contains some specific text replacements for Ukrainian
    schools datasets.

    Args:
        text: Text to shorten.

    Returns:
        str: Shortened text.
    """
    text = shorten(text)
    text = (
        text.replace("імені", "ім.")
        .replace("ступеня", "ступ")
        .replace("ступенів", "ступ")
        .replace("ступ.", "ступ")
        .replace("області", "обл")
        .replace("область", "обл")
        .replace("міста", "м")
        .replace("місто", "м")
        .replace("села", "с")
        .replace("село", "с")
        .replace("№", "")
        .replace("i", "і")
        .replace("фаховий", "")
        .replace("комунальнийзаклад", "")
    )
    return text
