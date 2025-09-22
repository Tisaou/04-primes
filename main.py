from math import sqrt

#### Fonction secondaire


def isprime(p):
    """Renvois vrai si p est un nombre premier """
    if p < 2:
        return False
    for d in range(2, int(sqrt(p)) + 1):
        if p % d == 0:
            return False
    return True

#### Fonction principale


def main():
    """Appel la fonction prime()"""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
