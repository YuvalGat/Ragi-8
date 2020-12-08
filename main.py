from dashes import *
from punctuation import *

# All correction methods
corrections = [correct_dashes, correct_punctuation]

# Apply all corrections
with open('./text.txt', 'r+') as file:
    text = file.read()
    for correction in corrections:
        text = correction(text)
    print(text)
