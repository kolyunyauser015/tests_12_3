import unittest
import running_tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = running_tournament.Runner('Усэйн', 10)
        self.runner_2 = running_tournament.Runner('Андрей', 9)
        self.runner_3 = running_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        list_participants = [self.runner_1, self.runner_3]
        tournament = running_tournament.Tournament(90, *list_participants)
        self.finishers = tournament.start()
        all_results = {n: self.finishers[n].name for n in self.finishers.keys()}
        self.assertTrue(all_results[len(list_participants)], 'Ник')
        TournamentTest.all_results[1] = all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        list_participants = [self.runner_3, self.runner_2]
        tournament = running_tournament.Tournament(90, *list_participants)
        self.finishers = tournament.start()
        all_results = {n: self.finishers[n].name for n in self.finishers.keys()}
        self.assertTrue(all_results[len(list_participants)], 'Ник')
        TournamentTest.all_results[2] = all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        list_participants = [self.runner_3, self.runner_2, self.runner_1]
        tournament = running_tournament.Tournament(90, *list_participants)
        self.finishers = tournament.start()
        all_results = {n: self.finishers[n].name for n in self.finishers.keys()}
        self.assertTrue(all_results[len(list_participants)], 'Ник')
        TournamentTest.all_results[3] = all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_4(self):
        list_participants = [self.runner_3, self.runner_2, self.runner_1]
        tournament = running_tournament.Tournament(90, *list_participants)
        self.finishers = tournament.start()
        for n in range(1, len(self.finishers)):
            self.assertGreaterEqual(self.finishers[n].speed, self.finishers[n+1].speed, None)

    @classmethod
    def tearDownClass(cls):
        print(*cls.all_results.values(), sep="\n")
