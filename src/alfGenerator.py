class ALFGenerator:
    def __init__(self, seed_list, j=55, k=24, bits=64):
        """
            seed_list: lista de sementes iniciais (precisa ter pelo menos j elementos)
            j: lag maior
            k: lag menor
            bits: numero máximo de bits dos números gerados
        """
        if len(seed_list) < j:
            raise ValueError("A lista de sementes precisa ter pelo menos j elementos.")
        
        self._buffer = seed_list.copy() # lista circular de tamanho fixo (objetivo é manter os últimos números necessários para a geração dos próximos números e reduzir o consumo de memória)
        self._j = j
        self._k = k
        self._m = 1 << bits             # 2**bits, porém mais rápido
        self._count = 0                 # Contador de números gerados

    def next(self):
        """
            Calcula e retorna o próximo número pseudo-aleatório.
        """
        # Calcula a posição no buffer a ser substituida
        i = self._count % len(self._buffer)

        # Calcula a posição de X_{n-j} e X_{n-k} no buffer
        j_idx = (self._count - self._j) % len(self._buffer)
        k_idx = (self._count - self._k) % len(self._buffer)
        
        # Calculando o próximo número pseudo-aleatório
        next_value = (self._buffer[j_idx] + self._buffer[k_idx]) % self._m

        # Substituindo no buffer
        self._buffer[i] = next_value

        # Acrescendo a contagem
        self._count += 1

        return next_value
