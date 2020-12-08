from correct_dashes import *

corrections = [correct_dashes]

with open('./text.txt', 'r+') as file:
    text = file.read()
    for correction in corrections:
        text = correction(text)
    print(text)
