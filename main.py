import os
import difflib

from corrections.dashes import *
from corrections.punctuation import *
from corrections.double_space import *
from corrections.initials import *
from corrections.period import *

# All correction methods
corrections = [correct_dashes, correct_punctuation, correct_double_space, correct_initials, correct_period]


def correct_text(text, corrections):
    corrected_text = text
    for correction in corrections:
        corrected_text = correction(corrected_text)

    return corrected_text


# Apply all corrections
with open('./text.txt', 'r+') as file:
    text = file.read()
    corrected_text = correct_text(text, corrections)

    with open('./corrected_text.txt', 'w') as corrected_file:
        corrected_file.write(corrected_text)

    d = difflib.HtmlDiff()
    diff = d.make_file(text.split('\n'), corrected_text.split('\n'))
    diff = diff.replace('<body>', '<body dir=\'rtl\'>')
    diff = diff.replace('(f)irst change', '<u>f</u>irst change')
    diff = diff.replace('(n)ext change', '<u>n</u>ext change')
    diff = diff.replace('(t)op', '<u>t</u>op')

    with open('./recommendations.html', 'w', encoding='utf-8') as recommendations_file:
        recommendations_file.write(diff)

    os.system('open recommendations.html')
