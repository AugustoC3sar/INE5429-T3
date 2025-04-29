import random

class MillerRabin:

    def is_prime(self, n: int) -> bool:
        """
        Parameters:
            n: número a ser testado (n > 2 e ímpar)

        Returns:
            - True, se n é provavelmente primo
            - False, se n é composto
        """

        # Caso base: 2 é primo
        if n == 2:
            return True

        # Se n é par ou menor que 2, não é primo
        if n < 2 or n % 2 == 0:
            return False
        
        # Escreve n-1 como 2^k * m com d ímpar
        k = 0
        m = n - 1
        while m % 2 == 0:
            m //= 2
            k += 1
        
        # Escolhe base aleatória
        a = random.randrange(2, n - 1)
        
        # Calcula a^m mod n
        x = pow(a, m, n)

        # Se a^m mod n == 1 ou a^m mod n == -1, então é provavelmente primo
        if x == 1 or x == n - 1:
            return True

        # Caso contrário, para i de 0 até k-1
        for _ in range(k - 1):
            # Calcula a^((2^i)*m) mod n
            x = pow(x, 2, n)

            # Se for igual a n-1, então é provavelmente primo
            if x == n - 1:
                return True
    
        return False  # Se nunca encontrou n-1, n é composto

    def is_prime_k_times(self, n:int, k:int) -> bool:
        """
            Verifica se um dado n é um número primo, aplicando o teste de miller-rabin por k vezes.

            Parameters:
                - n: número a ser testado
                - k: número de iterações
            
            Returns:
                - True, se n passar em todos os testes, configurando que n é provavelmente primo
                - False, se n falhar em algum teste
        """
        for _ in range(k):
            if not self.is_prime(n):
                return False  # Se em algum teste for composto, já retorna False
        return True  # Se passar em todos, provavelmente primo