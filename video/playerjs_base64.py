from base64 import b64encode, b64decode
import random
from JKSite.settings import PJS_BASE64_SEPARATOR, PJS_BASE64_KEYS

def pjs_b64_encrypt(string):
    result = b64encode(bytes(string, 'utf-8'))
    for key in PJS_BASE64_KEYS:
        if key:
            rand_index = random.randint(0, len(result))
            result = result[:rand_index] + PJS_BASE64_SEPARATOR + b64encode(bytes(key, "utf-8")) + result[rand_index:]
    return (b"#2" + result).decode("utf-8")


def pjs_b64_decrypt(string):
    result = string.encode("utf-8")
    for key in PJS_BASE64_KEYS[::-1]:
        if key:
            result = result.replace(PJS_BASE64_SEPARATOR + b64encode(bytes(key, "utf-8")), b"")
    result = b64decode(result[2:])
    return result.decode("utf-8")
