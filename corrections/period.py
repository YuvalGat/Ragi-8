import re


def correct_period(text):
    """

    :param text: text to be corrected
    :return: text where newlines are always preceded by a period, unless preceded by question mark
    """
    period_end_of_sentence_regex = r'(?<!\.)\n'
    text = re.sub(period_end_of_sentence_regex, r'.\n', text)
    question_mark_period_regex = r'\?\.'
    text = re.sub(question_mark_period_regex, r'?', text)
    return text
