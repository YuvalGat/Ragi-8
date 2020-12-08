import re

def correct_dashes(text):
    dashes_regex = r'([בכמלו])(\d)'
    text = re.sub(dashes_regex, r'\1-\2', text)
    return text