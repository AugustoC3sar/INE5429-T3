from src.fermat import FermatTest
from src.mwcGenerator import MWCGenerator
import random

import pandas as pd
import datetime
import time


class TestFermatTest:

    output_dir = "."

    def __init__(self):
        self._seeds = dict()
    
    def set_seeds(self, n_bits_list: list[int]) -> None:
        random.seed(42)
        for n in n_bits_list:
            self._seeds[f"{n}"] = random.getrandbits(n)

    def gera_primo_n_bits(self, n: int) -> tuple[int, float]:
        # Setup
        random.seed(42)
        seed = random.getrandbits(n)
        gen = MWCGenerator(seed, bits=n)
        fermat_test = FermatTest()
        start_time = time.time() * 1000 # ms
        
        # Execution
        while True:
            num = 1
            while num % 2 != 1 or num.bit_length() != n:
                num = gen.next()
            if fermat_test.is_prime(num, 5):
                break

        # Results
        runtime = (time.time() * 1000) - start_time

        return (num, runtime)

    def test_gera_primo_n_bits(self):
        print("[RUNNING] test_gera_primo_n_bits")

        # Setup
        n_bits_list = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
        self.set_seeds(n_bits_list)

        columns = ["N bits", "Número", "Tempo"]
        df = pd.DataFrame(columns=columns)

        for n in n_bits_list:
            num, runtime = self.gera_primo_n_bits(n)
            row = {"N bits": n, "Número": str(num), "Tempo": f"{runtime:.8f} ms"}
            df = pd.concat([df, pd.DataFrame([row])])    

        str_datetime = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        output_file = f"{__class__.output_dir}/Fermat_MWC_k_numeros_n_bits_at_{str_datetime}.csv"
        df.to_csv(output_file, sep=";", decimal=",", encoding="utf-8", index=False)

        print("[    OK ] test_gera_primo_n_bits")
    
    def run(self):
        print("==== Running Fermat Test tests ====")

        self.test_gera_primo_n_bits()