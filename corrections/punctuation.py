import re


def correct_punctuation(text):
    """

    :param text: text to be corrected
    :return: text with properly spaced punctuation
    """
    punctuation_regex = r'([\.,;\'\)\?\!])([א-ת0-9])'  # Fix spacing after punctuation...
    text = re.sub(punctuation_regex, r'\1 \2', text)
    digit_punctuation_regex = r'(\d)([,.]) (\d)'  # ...unless it is a comma or period in a decimal number
    text = re.sub(digit_punctuation_regex, r'\1\2\3', text)
    opening_parentheses_regex = r'([א-ת0-9])\('  # Ensure space before opening parentheses
    text = re.sub(opening_parentheses_regex, r'\1 (', text)
    question_mark_space_regex = r' \?'  # Ensure no space before question mark
    text = re.sub(question_mark_space_regex, '?', text)
    return text
