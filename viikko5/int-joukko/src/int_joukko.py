class IntJoukko:
    def __init__(self, a=None, b=None):
        self.int_list = []

    def kuuluu(self, n):
        if n in self.int_list:
            return True
        return False

    def lisaa(self, n):
        if n in self.int_list:
            return False
        self.int_list.append(n)
        return True

    def poista(self, n):
        if n in self.int_list:
            self.int_list.remove(n)
            return True
        return False

    def mahtavuus(self):
        return len(self.int_list)

    def to_int_list(self):
        return self.int_list
    
    @staticmethod
    def setup_calc(a, b):
        return IntJoukko(), a.to_int_list(), b.to_int_list()

    @staticmethod
    def yhdiste(a, b):
        x, a_taulu, b_taulu = IntJoukko.setup_calc(a, b)

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y, a_taulu, b_taulu = IntJoukko.setup_calc(a, b)

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z, a_taulu, b_taulu = IntJoukko.setup_calc(a, b)

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        return "{" + ", ".join(str(i) for i in self.int_list) + "}"
