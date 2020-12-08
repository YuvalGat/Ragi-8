import re


def correct_double_space(text):
    """

    :param text: text to be corrected
    :return: text where double spaces are replaced with a single space
    """
    double_space_regex = r'\s\s+'
    text = re.sub(double_space_regex, ' ', text)
    return text
