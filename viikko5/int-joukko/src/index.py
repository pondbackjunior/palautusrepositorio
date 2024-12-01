import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)

    print(joukko.to_int_list())
    print(joukko)

    joukko.poista(2)
    print(joukko.kuuluu(2))
    print(joukko)

if __name__ == "__main__":
    main()
