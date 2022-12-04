def read(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    lines = [line.rstrip() for line in lines]  # remove newline characters
    return lines

