import unittest
import test_12_1
import test_12_2

is_frozen = True
suiteT = unittest.TestSuite()
suiteT.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
suiteT.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suiteT)
