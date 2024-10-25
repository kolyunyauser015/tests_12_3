import unittest
import running_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = running_tournament.Runner('Maxim', 5)
        for n in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = running_tournament.Runner('Oleg', 5)
        for n in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = running_tournament.Runner('Olga', 5)
        runner_4 = running_tournament.Runner('Petr', 7)
        for n in range(10):
            runner_3.walk()
            runner_4.walk()
        d_1 = runner_3.distance
        d_2 = runner_4.distance
        for n in range(10):
            runner_3.run()
            runner_4.run()
        d_3 = runner_3.distance
        d_4 = runner_4.distance
        self.assertNotEqual(d_1, d_3)
        self.assertNotEqual(d_2, d_4)
        self.assertNotEqual(d_1, d_2)
        self.assertNotEqual(d_3, d_4)


