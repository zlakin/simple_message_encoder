import sys
import base64
script, input_encoding, error = sys.argv


def main(textfile, encoding, errors):
    line = textfile.readline()
    if line:
        print_line(line, encoding, errors)
        return main(textfile, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    byte_string = base64.b64encode(next_lang.encode("utf-8"))
    secret_message = str(byte_string, "utf-8")
    decoded_bytes = base64.b64decode(byte_string.decode("utf-8"))
    decoded_msg = str(decoded_bytes, "utf-8")
    print(secret_message, "<=====>", decoded_msg)


languages = open("secret_message.txt", encoding="utf-8")
main(languages, input_encoding, error)
