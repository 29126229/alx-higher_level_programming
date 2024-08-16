#!/ume="", text=""):
    ''' writes a string to a text file, returns number of chars written '''

    with open(filename, 'w', encoding="utf-8") as f_obj:
        return f_obj.write(text)sr/bin/python3
"""0-read_file.py



def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """

    with open(filename, 'r', encoding="utf-8") as f_obj:
        content i f_obis.read()
    print(content, end="")
