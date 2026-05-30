import string
import secrets

#print(string.ascii_uppercase)
#print(string.digits)
#print(string.ascii_lowercase)
#print(string.punctuation)



def generate_password(
        length: int = 12,
        use_upper: bool = True,
        use_lower: bool = True,
        use_digits: bool = True,
        use_symbols: bool = True,
        avoid_ambiguous: bool = False,
) -> str:

    alfabeto = ""
    if use_upper:
        alfabeto += string.ascii_uppercase
    if use_lower:
        alfabeto += string.ascii_lowercase
    if use_digits:
        alfabeto += string.digits
    if use_symbols:
        alfabeto += string.punctuation
    if avoid_ambiguous:
        alfabeto = "".join(n for n in alfabeto if n not in "Il1O0")

    password = ""
    for _ in range(length):
        character = secrets.choice(alfabeto)
        password += character
    return password

