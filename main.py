import random
import string

def password(length=16):
    switcher = {
        1: string.ascii_lowercase,
        2: string.ascii_uppercase,
        3: string.digits,
        4: string.punctuation
    }

    def new_char():
        return random.choice(switcher[random.randint(1, 4)])

    return ''.join(new_char() for _ in range(length))

print(password())
print(password(8))



# import random
# import string
#
# def password(length=16):
#     modes = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
#     chars = []
#     for i in range(length):
#         chars.append(random.choice(random.choice(modes)))
#
#     return ''.join(chars)
#
# print(password())
# print(password(8))