def correct_initials(text):
    """

    :param text: text to be corrected
    :return: text which has initials properly quoted
    """
    with open('./corrections/initials.txt', 'r') as initials_file:
        initials = initials_file.read().split('\n')
        print(initials)
        for initial in initials:
            quoted = f'{initial[:-1]}"{initial[-1:]}'
            print(quoted)
            for prefix in ['', 'ב', 'ל', 'כ', 'ו', 'ה', 'מ', ')']:
                text = text.replace(prefix + initial + ' ', quoted + ' ')

    return text
