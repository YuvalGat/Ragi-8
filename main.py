import os

from dashes import *
from punctuation import *
from double_space import *

# All correction methods
corrections = [correct_dashes, correct_punctuation, correct_double_space]

# Apply all corrections
with open('./text.txt', 'r+') as file:
    text = file.read()
    corrected_text = text
    for correction in corrections:
        corrected_text = correction(corrected_text)

    with open('./corrected_text.txt', 'w') as corrected_file:
        corrected_file.write(corrected_text)

    print(corrected_text)
