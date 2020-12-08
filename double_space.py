import re


def correct_double_space(text):
    double_space_regex = r'  '
    text = re.sub(double_space_regex, ' ', text)
    return text