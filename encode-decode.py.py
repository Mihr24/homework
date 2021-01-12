def encode_string(text: str):
    result = ""
    for latter in text:
        binnumber = ('{:08b}'.format(ord(latter)))
        result += str(binnumber)
    return result


def decode_string(code):
    i = 0
    result = ""
    while (i + 8) <= (len(code)):
        symbol = int(code[i:i + 8], 2)
        result += chr(symbol)
        i += 8
    return result
