import re


def correct_dashes(text):
    dashes_regex = r'([בכמלו])(\d)'
    text = re.sub(dashes_regex, r'\1-\2', text)
    return text


with open('./text.txt', 'r+') as file:
    text = file.read()
    text = correct_dashes(text)
    print(text)
