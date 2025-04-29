from src.mwcGenerator import MWCGenerator
import time
import pandas as pd
import datetime


class TestMWCGenerator:
    output_dir = "."
    debug = False

    def log(self, lvl:str, msg:str) -> None:
        if self.debug:
            print(f"[{lvl}]: {msg}")

    def gera_numero_n_bits_com_seed(self, seed:int, n:int) -> tuple[float, float]:
        """
            Método para gerar um número de n bits significativos, utilizando uma dada seed no MWC Generator

            Retorna o número de n bits e o tempo necessário para sua geração
        """
        # Setup
        gen = MWCGenerator(seed, bits=n)
        start_time = time.time() * 1000 # ms
        num = 0

        # Execution
        while num.bit_length() != n:
            num = gen.next()
        
        # Results
        runtime = (time.time() * 1000) - start_time

        return (num, runtime)

    def gera_k_numeros_n_bits(self, k: int, n: int) -> float:
        """
            Método para gerar k números de n bits significativos, utilizando uma seed fixa no MWC Generator

            Retorna o tempo médio decorrido para geração dos k números
        """
        # Setup
        seed = 12345
        gen = MWCGenerator(seed, bits=n)
        sum_runtime = 0
        num = 0

        # Execution
        for i in range(k):
            start_time = time.time() * 1000 # ms
            
            while num.bit_length() != n:
                num = gen.next()
                
            runtime = (time.time() * 1000) - start_time

            sum_runtime += runtime

        # Results
        mean_time = sum_runtime / k

        return mean_time

    def test_gera_numero_n_bits_com_seed(self):
        print("[RUNNING] test_gera_numero_n_bits_com_seed")

        # Setup
        seeds = [1, 42, 12345, 16777216, 2147483647, 987654321, 1000000007, 4294967295, 18446744073709551615]
        n_bits_list = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

        columns = ["seeds"] + [f"{n} bits" for n in n_bits_list]
        df = pd.DataFrame(columns=columns)

        # Execution
        for seed in seeds:
            row = {"seeds": seed}

            for n in n_bits_list:
                _, runtime = self.gera_numero_n_bits_com_seed(seed, n)
                row[f"{n} bits"] = f"{runtime:.8f}"
            
            df = pd.concat([df, pd.DataFrame([row])])
        
        # Results
        str_datetime = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        output_file = f"{__class__.output_dir}/MWC_numero_n_bits_seed_at_{str_datetime}.csv"
        df.to_csv(output_file, sep=";", decimal=",", encoding="utf-8", index=False)
        
        print("[    OK ] test_gera_numero_n_bits_com_seed")

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
        output_file = f"{__class__.output_dir}/MWC_k_numeros_n_bits_at_{str_datetime}.csv"
        df.to_csv(output_file, sep=";", decimal=",", encoding="utf-8", index=False)

        self.log("INFO", f"Results exported on '{output_file}'")

        print("[    OK ] test_gera_k_numeros_n_bits")

    def run(self):
        print("==== Running MWCGenerator tests ====\n\n")
        
        self.test_gera_k_numeros_n_bits()
        self.test_gera_numero_n_bits_com_seed()
