def get_file(file):
    result = ''
    with open(file) as f:
        for line in f:
            result += line
    f.close()
    return result
