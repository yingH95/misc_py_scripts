import string


def read_eng(file):
    new_file = ""
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line != "" and line[0] != '<':
                if line[0] in string.ascii_letters or line[0] in string.punctuation:
                    new_file += line + '\n'
    return new_file
