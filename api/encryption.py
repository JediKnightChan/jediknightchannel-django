from cryptography.fernet import Fernet

ENCRYPTION_KEY = b'-W0Ygb_Ra_GZsvvUSpy7CFNSxfXdmBc1vHp8nOHuRFs='
CIPHER_SUITE = Fernet(ENCRYPTION_KEY)


def encrypt_byte_string(byte_string):
    return CIPHER_SUITE.encrypt(byte_string).decode("utf-8")


def decrypt_to_byte_string(encoded_data):
    encoded_data = encoded_data.encode("utf-8")
    return CIPHER_SUITE.decrypt(encoded_data)


def compare_s(str1, str2):
    if len(str1) != len(str2):
        print("Diff lens", len(str1), len(str2))
        print(str1)
        print(str2)
        return False
    for i in range(len(str1)):
        c1 = str1[i]
        c2 = str2[i]
        if c1 != c2:
            print("Chars in " + str(i) + ": " + c1 + " " + c2)
            print(str1)
            print(str2)
            return False
    return True