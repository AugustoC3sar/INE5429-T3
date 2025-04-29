from tests.testMwcGenerator import TestMWCGenerator
from tests.testAlfGenerator import TestALFGenerator
from tests.testMillerRabin import TestMillerRabin
from tests.testFermat import TestFermatTest

import os

def main():
    # Creating output dir
    output_dir = "./output"

    os.makedirs(output_dir, exist_ok=True)
    
    # Setting up test classes
    TestMWCGenerator.output_dir = output_dir
    TestALFGenerator.output_dir = output_dir
    TestMillerRabin.output_dir = output_dir
    TestFermatTest.output_dir = output_dir
    
    # Testing objects
    mwc_test = TestMWCGenerator()
    alf_test = TestALFGenerator()
    mr_test = TestMillerRabin()
    fermat_test = TestFermatTest()

    # Running tests
    mwc_test.run()
    alf_test.run()
    mr_test.run()
    fermat_test.run()


if __name__ == "__main__":
    main()