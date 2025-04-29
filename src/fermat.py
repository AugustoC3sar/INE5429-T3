import random

class FermatTest:

    def is_prime(self, n: int, k: int) -> bool:
        """ 
            Parameters:
                - n: número a ser testado.
                - k: número de testes (bases aleatórias).

            Returns:
                - True se n é provavelmente primo.
                - False se n é composto.
        """

        # Se n <= 1, então n não é primo
        if n <= 1:
            return False
        
        # Caso base: 2 é primo
        if n == 2:
            return True

        # Para k iterações
        for _ in range(k):
            # Gera uma base aleatória (a)
            a = random.randint(2, n-2)

            # Se a^(n-1) mod n != 1, então n é composto
            if pow(a, n-1, n) != 1:
                return False
        
        # Se passou em todos os k testes, então n é provavelmente primo 
        return True