import re


def correct_dashes(text):
    """

    :param text: text to be corrected
    :return: text where letters followed by numbers are properly hyphened
    """
    dashes_regex = r'([בכמלו])(\d)'
    text = re.sub(dashes_regex, r'\1-\2', text)
    return text
