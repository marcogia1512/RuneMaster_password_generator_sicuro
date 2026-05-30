import string
import secrets
from pathlib import Path

def generate_password(
        length: int = 12,
        use_upper: bool = True,
        use_lower: bool = True,
        use_digits: bool = True,
        use_symbols: bool = True,
        avoid_ambiguous: bool = False,
) -> str:

    alphabet = ""
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_lower:
        alphabet += string.ascii_lowercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation
    if avoid_ambiguous:
        alphabet = "".join(n for n in alphabet if n not in "Il1O0")

    if not alphabet:
        raise ValueError("Empty alphabet")

    set_true = use_upper + use_lower + use_digits + use_symbols

    if length < set_true:
        raise ValueError("Increase length your password")

    password = []
    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))
    for _ in range(length - set_true):
        password.append(secrets.choice(alphabet))
    secrets.SystemRandom().shuffle(password)
    password = "".join(password)
    return password

if __name__ == "__main__":
    print("=== Password generator ===")
    print("1) Profilo default (12 caratteri, tutti i set, visualizza a schermo")
    print("2) Profilo custom")
    choice = input("Scelta: ")
    if choice == "1":
        print(f"Password generata: {generate_password()}")
    elif choice == "2":
        use_upper = input("Maiuscole? (y/n) [y]: ") == "y"
        use_lower = input("Minuscole? (y/n) [y]: ") == "y"
        use_digits = input("Cifre? (y/n) [y]: ") == "y"
        use_symbols = input("Simboli? (y/n) [y]: ") == "y"
        length = int(input("Lunghezza [12]: "))
        avoid_ambiguous = input("Evitare caratteri ambigui? (y/n) [y]: ") == "y"
        save_password = input("Salvare su file? (y/n) [y]: ") == "y"
        password_generated = generate_password(length=length, use_upper=use_upper, use_lower=use_lower,
                                               use_digits=use_digits, use_symbols=use_symbols,
                                               avoid_ambiguous=avoid_ambiguous)
        print(f"Password generata: {password_generated}")
        if save_password:
            file = input("Percorso del file: ")
            Path(file).expanduser().write_text(password_generated)
            print(f"Salvata in {file}")


