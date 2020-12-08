import re


def correct_punctuation(text):
    """

    :param text: text to be corrected
    :return: text with properly spaced punctuation
    """
    punctuation_regex = r'([\.,;\'\)\?\!])([א-ת0-9])'
    text = re.sub(punctuation_regex, r'\1 \2', text)
    digit_punctuation_regex = r'(\d), (\d)'
    text = re.sub(digit_punctuation_regex, r'\1,\2', text)
    return text
