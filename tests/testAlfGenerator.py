import time
import pandas as pd
import datetime
import random

from src.alfGenerator import ALFGenerator

class TestALFGenerator:
    output_dir = "."
    debug = False

    def __init__(self):
        random.seed(42)
        self._seeds = [random.getrandbits(32) for _ in range(55)]
        print(self._seeds)

    def log(self, lvl:str, msg:str):
        if self.debug:
            print(f"[{lvl}]: {msg}")

    def gera_k_numeros_n_bits(self, k: int, n_bits: int) -> float:
        # Setup
        gen = ALFGenerator(self._seeds, bits=n_bits)
        sum_runtime = 0

        # Execution
        for _ in range(k):
            start = time.time() * 1000
            
            while True:
                num = gen.next()
                if num.bit_length() == n_bits:
                    runtime = (time.time() * 1000) - start
                    break
            
            sum_runtime += runtime

        mean_time = sum_runtime / k

        return mean_time

    def test_gera_k_numeros_n_bits(self):
        print("[RUNNING] test_gera_k_numeros_n_bits")

        # Setup
        k_list = [1, 50, 100, 500, 1000, 5000]
        n_bits_list = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

        columns = ["N bits"] + [f"{k} número(s)" for k in k_list]
        df = pd.DataFrame(columns=columns)

        # Execution
        for n in n_bits_list:
            row = {"N bits": n}

            for k in k_list:
                runtime = self.gera_k_numeros_n_bits(k, n)
                row[f"{k} número(s)"] = f"{runtime:.8f} ms"
                self.log("INFO", f"Finished generating {k} numbers with {n} bits")
            
            df = pd.concat([df, pd.DataFrame([row])])

        # Results
        str_datetime = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        output_file = f"{__class__.output_dir}/MWC_k_numeros_numeros_primos_n_bits_{str_datetime}.csv"
        df.to_csv(output_file, sep=";", decimal=",", encoding="utf-8", index=False)


        print("[    OK ] test_gera_k_numeros_n_bits")

    def run(self):
        print("==== Running ALFGenerator tests ====")

        self.test_gera_k_numeros_n_bits()