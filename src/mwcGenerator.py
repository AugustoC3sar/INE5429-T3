class MWCGenerator:
    def __init__(self, seed:int, carry: int = 0, a: int = 4294957665, bits: int = 64):
        self._xn = seed
        self._cn = carry
        self._a = a
        self._b = 1 << bits # 2**bits, porém mais rápido
        self._bits_per_step = bits

    def next(self) -> int:
        # Colocando a parte utilizada em ambas as fórmulas (a . X_{n-1} + c_{n-1}) em uma variável
        t = self._a * self._xn +  self._cn

        # Calculando o pŕóximo número aleatório
        self._xn = t % self._b

        # Calculando o próximo carry
        self._cn = t // self._b

        # Último número da lista sempre vai ser o número gerado
        return self._xn
